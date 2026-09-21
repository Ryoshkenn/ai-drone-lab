# Experiment: environment smoke test

- Date/time: 2026-09-20 17:03 PDT
- Operator: Jagruth Gajula, with Codex assistance
- Git commit: `ff7975757669d318fd28cf4618e97597c6c3d1f3`
- Phase: 0 — Reproducible baseline
- Status: complete

## Question

Can a clean, pinned Python 3.12 environment initialize and step the selected simulator headlessly, and does the project smoke command produce repeatable summaries for identical seeds on this machine?

## Hypothesis

The environment will initialize and two seed-0 random-action runs will produce identical compact summaries. A random controller is expected to violate a termination boundary before the full 30 steps and is not expected to hover.

## Configuration

- Environment: `gym-pybullet-drones` 2.2.0 at commit `7ebad1ecabd28a7000add2d05f888aa2e837c2cc`
- Python: 3.12.14
- Observation: upstream `HoverAviary` kinematic observation, shape `(1, 72)`
- Action: upstream direct RPM action, normalized `[-1, 1]`, shape `(1, 4)`
- Controller: NumPy seed-0 uniform random actions
- Requested horizon: 30 control steps
- Hardware: AMD Ryzen 5 5600H; 12 GiB visible memory; CPU-only PyTorch environment

## Commands

```bash
uv sync --extra dev
uv run pytest
uv run ruff check .
uv run neuroflight-smoke --steps 30 --seed 0 > work/smoke-a.json
uv run neuroflight-smoke --steps 30 --seed 0 > work/smoke-b.json
uv run python -c 'import json; json.load(open("work/smoke-a.json", encoding="utf-8"))'
diff -u work/smoke-a.json work/smoke-b.json
```

## Results

- Unit tests: 4 passed.
- Lint: passed.
- Both smoke summaries were byte-for-byte identical.
- Both runs executed 13 of 30 requested steps and then truncated.
- Initial observation digest: `cdb65770ab4e5fb1`.
- Final observation digest: `f10c551ea4957f9a`.
- Total upstream reward before truncation: `17.74149663`.
- Compact machine-readable output: [`summary.json`](summary.json).

The upstream environment emitted warnings that float64 Box bounds were cast to float32. They did not prevent execution, but the observation/action-space construction should be inspected during the environment audit.

## Interpretation

This passes the narrow integration check: the pinned simulator can execute headlessly and identical inputs produced identical summaries on the same machine. It does not show that training works, that cross-machine results are bitwise deterministic, or that any policy can hover.

The early truncation is expected evidence of an ineffective random controller, not a regression and not a baseline score suitable for comparison yet.

## Follow-up

Benchmark headless simulation throughput and reproduce the upstream PPO hover example, recording training/evaluation seeds, wall-clock time, and aggregate metrics.
