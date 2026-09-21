# ADR 0002: Pin Python 3.12 and the simulator revision

- Status: proposed
- Date: 2026-09-20

## Context

The development laptop currently exposes Python 3.14.4. The maintained simulator declares Python 3.12 compatibility, and native scientific dependencies can lag new Python releases. Depending on the moving upstream `main` branch would also make old experiment environments difficult to reconstruct.

## Decision

Use an isolated Python 3.12 environment managed with `uv`. Pin `gym-pybullet-drones` to commit `7ebad1ecabd28a7000add2d05f888aa2e837c2cc` for Phase 0.

## Consequences

- Setup downloads a separate Python runtime and does not modify the system Python.
- Updating the simulator requires an explicit dependency change and a new validation run.
- Exact reproduction still depends on recording the generated lockfile, OS, architecture, and hardware.
