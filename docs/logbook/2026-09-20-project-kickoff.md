# Project kickoff — 2026-09-20

## Objective

Turn the initial autonomous FPV-drone learning concept into a scoped, reproducible GitHub project with an achievable first milestone.

## Work completed

- Reduced the first milestone to state-based hover before navigation, gates, vision, or physical flight.
- Selected `gym-pybullet-drones` as the proposed first simulator and standard PPO as the reference baseline.
- Added a milestone roadmap, safety boundary, experiment template, and decision-record workflow.
- Pinned Python and the proposed upstream simulator revision.
- Added a headless random-action smoke test and unit tests for its compact summary.

## Machine snapshot

- OS: Ubuntu 26.04 LTS, x86-64
- CPU: AMD Ryzen 5 5600H, 6 cores / 12 threads
- Memory visible during kickoff: 12 GiB
- GPU: NVIDIA GeForce GTX 1650, 4 GiB
- System Python: 3.14.4 (not used for the pinned project environment)
- `ffmpeg`: available

This snapshot describes the machine used during kickoff, not a minimum requirement.

## Evidence status

No learning experiment has been completed. The first committed execution evidence should be the Phase 0 smoke-test manifest, followed by an upstream PPO reproduction.

## Setup observations

The first `uv sync --extra dev` attempt resolved the pinned dependency graph but stopped while building this local package because Hatch requires an explicit opt-in for direct Git references. Resolution also selected CUDA-enabled PyTorch packages by default. The project configuration was corrected to permit the pinned simulator reference and use PyTorch's CPU wheel index for the CPU-first baseline. This was an environment-setup failure, not a simulator or learning result.

## Open owner decisions

- Accept or rename the working title “NeuroFlight Lab.”
- Accept or revise ADRs 0001 and 0002.
- Select a license before inviting reuse or contributions.
- Decide the time budget and cadence for Phase 0.

## Next action

Create and run the isolated environment, commit the resulting lockfile, execute the smoke test twice with the same seed, and record the outputs in an experiment manifest.
