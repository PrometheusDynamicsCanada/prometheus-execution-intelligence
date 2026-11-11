#!/usr/bin/env python3
"""
Standalone offline verifier for `prometheus-execution-intelligence`:
1. Audits `PORTFOLIO_ACCOUNTING_LEDGER.json` arithmetic and verifies that all
   405 provider Job IDs / AWS Braket Task ARNs are strictly unique (zero cross-campaign
   duplicates), with shared reference suites (`qpu-selection-execution-quality` 33 ZIPs
   and the 4-job 144-execution suite) explicitly cross-mapped and counted once.
2. Verifies byte-for-byte SHA-256 integrity of all tracked files in `REPO_SHA256_MANIFEST.json`.
"""

import hashlib
import json
from pathlib import Path


def sha256_bytes(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    ledger_path = root / "PORTFOLIO_ACCOUNTING_LEDGER.json"
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))

    totals = ledger["portfolio_totals"]
    repos = ledger["constituent_repositories"]
    assert len(repos) == totals["quantum_repositories_total"] == 10

    rec_sum = sum(int(r["incremental_provider_records"]) for r in repos)
    bench_sum = sum(int(r["incremental_benchmark_jobs"]) for r in repos)
    aux_sum = sum(int(r["incremental_auxiliary_records"]) for r in repos)
    pub_sum = sum(int(r["incremental_physical_pubs"]) for r in repos)
    shot_sum = sum(int(r["incremental_physical_shots"]) for r in repos)

    assert rec_sum == totals["unique_provider_records"] == 405
    assert bench_sum == totals["completed_benchmark_jobs_or_tasks"] == 397
    assert aux_sum == totals["auxiliary_warmup_or_troubleshooting_records"] == 8
    assert bench_sum + aux_sum == rec_sum
    assert pub_sum == totals["physical_circuits_or_pubs"] == 7619
    assert shot_sum == totals["physical_measurement_shots"] == 15358208

    # Provider-family breakdown
    p_ibm = totals["ibm_quantum_records"]
    p_aws = totals["aws_braket_programset_tasks"]
    p_iqm = totals["iqm_resonance_records"]
    assert p_ibm["total"] + p_aws["total"] + p_iqm["total"] == 405
    assert p_ibm["benchmark_jobs"] + p_aws["benchmark_tasks"] + p_iqm["benchmark_jobs"] == 397
    assert p_ibm["auxiliary_records"] + p_aws["auxiliary_records"] + p_iqm["auxiliary_records"] == 8

    # Strict cross-repository deduplication check across all 405 IDs
    all_ids = []
    by_repo = {}
    for r in repos:
        uids = r["unique_provider_ids"]
        assert len(uids) == int(r["incremental_provider_records"]), (
            f"{r['repository']}: expected {r['incremental_provider_records']} IDs, found {len(uids)}"
        )
        assert len(set(uids)) == len(uids), f"Duplicate ID inside {r['repository']}"
        by_repo[r["repository"]] = set(uids)
        all_ids.extend(uids)

    assert len(all_ids) == 405 and len(set(all_ids)) == 405, (
        f"Cross-repository duplicate Job ID detected: {len(all_ids)} total vs {len(set(all_ids))} unique"
    )

    # Verify shared reference subsets map 100% to their primary counting repositories
    for r in repos:
        shared = r.get("shared_reference_ids_counted_elsewhere", {})
        for target_key, ref_ids in shared.items():
            target_repo = target_key.replace("counted_in_", "")
            assert set(ref_ids).issubset(by_repo[target_repo]), (
                f"{r['repository']} shared IDs not subset of {target_repo}"
            )

    print("=" * 92)
    print("PORTFOLIO ACCOUNTING & CROSS-REPOSITORY JOB-ID DEDUPLICATION AUDIT")
    print("=" * 92)
    print(f"  [PASS] Quantum Repositories Indexed      : {len(repos)}")
    print(f"  [PASS] Unique Provider Records Verified  : {len(set(all_ids))} / 405 (0 duplicates; {bench_sum} bench + {aux_sum} aux)")
    print(f"  [PASS] Physical Circuits / PUBs Verified : {pub_sum:,d}")
    print(f"  [PASS] Physical Shots Verified           : {shot_sum:,d}")

    manifest_path = root / "REPO_SHA256_MANIFEST.json"
    if manifest_path.exists():
        rm = json.loads(manifest_path.read_text(encoding="utf-8"))
        for rel_p, exp_sha in rm["files"].items():
            fp = root / rel_p
            act_sha = sha256_bytes(fp)
            assert act_sha == exp_sha, f"SHA-256 mismatch on {rel_p}: {act_sha} != {exp_sha}"
        print(f"  [PASS] REPO_SHA256_MANIFEST.json         : {len(rm['files'])} / {len(rm['files'])} files match byte-for-byte")
    print("=" * 92)


if __name__ == "__main__":
    main()
