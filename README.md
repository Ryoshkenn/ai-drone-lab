# NeuroFlight Lab

NeuroFlight Lab is a reproducible research project exploring whether a small neural network can learn general quadrotor flight-control behavior from randomly initialized weights in simulation.

The project begins with a deliberately narrow target: **learn a stable 10-second hover from varied starting positions and orientations using numerical state observations**. Gate navigation, camera-only control, simulator transfer, and physical flight are later milestones—not claims about the current system.

> Status: Phase 0 — environment and baseline validation. No trained policy or real-world flight result exists yet.

## Research question

Can a drone learn general flight-control behavior from scratch in simulation, then retain useful behavior under unseen initial conditions, dynamics, and environments?

“From scratch” means the policy and value networks begin with random weights. The physics engine and, initially, a standard PPO implementation are established dependencies. This distinction keeps the claim precise and testable.

## Milestone ladder

| Phase | Deliverable | Evidence required to complete it |
|---|---|---|
| 0. Reproduce | Headless simulator smoke test and upstream hover baseline | Environment manifest, command log, metrics, and repeatable setup |
| 1. Hover | State-based PPO policy holds a 10-second hover | Held-out evaluation over multiple seeds and randomized starts |
| 2. Navigate | Policy reaches arbitrary 3D targets | Success rate, path error, time-to-target, and crash rate |
| 3. Gates | Policy traverses unseen gate layouts | Gate completion and collision metrics on held-out courses |
| 4. Vision | Policy acts from FPV images rather than privileged state | Comparison with the state-based policy and ablations |
| 5. Transfer | Policy is evaluated in a second simulator | Documented interface, domain gap, and transfer results |
| 6. Physical | Carefully gated real-platform experiment | Separate safety review and explicit go/no-go approval |

The detailed criteria and stop conditions live in [the roadmap](docs/ROADMAP.md).

## Quick start

This repository pins Python 3.12 and the exact simulator revision used for the first experiments. [`uv`](https://docs.astral.sh/uv/) is the recommended environment manager.

```bash
uv sync --extra dev
uv run pytest
uv run ruff check .
uv run neuroflight-smoke --steps 30 --seed 0
```

The smoke test uses random actions. It validates the integration; it is not a learning result.

## How results will be documented

Every meaningful experiment gets:

1. A dated entry in [`docs/logbook`](docs/logbook/README.md).
2. A tracked manifest based on [`experiments/TEMPLATE.md`](experiments/TEMPLATE.md).
3. The exact Git commit, random seeds, configuration, hardware, and commands.
4. Aggregate metrics and failure cases—not only the best video.
5. A clear separation between training, validation, and held-out evaluation.

Large checkpoints, raw logs, and videos are intentionally excluded from Git. Compact manifests, plots, tables, and selected media can be committed when they are useful evidence.

## Current technical direction

- Python 3.12, PyTorch, Gymnasium, and Stable-Baselines3
- `gym-pybullet-drones` as the first physics environment
- Kinematic observations before camera observations
- Standard PPO as a reference baseline before a custom implementation
- CPU-first benchmarking; GPU use only when profiling supports it

Key design choices are recorded as short [architecture decision records](docs/decisions/README.md), so changes in direction remain visible.

## Safety boundary

All current work is simulation-only. Physical flight is out of scope until the project passes the explicit prerequisites in [SAFETY.md](docs/SAFETY.md). The project will not test around people, animals, traffic, or uncontrolled airspace.

## Project integrity

The repository is designed to show the work through reproducible commits and evidence. It does not present planned milestones as completed results. Tool assistance and ownership are recorded in [PROVENANCE.md](docs/PROVENANCE.md).

## License

No license has been selected yet. Until the owner chooses one, normal copyright rules apply.

