# Safety policy

## Current boundary

The current project is simulation-only. The repository may model flight and train policies, but it does not authorize testing a learned controller on a physical aircraft.

## Requirements before any powered physical test

All items require explicit review and a recorded go/no-go decision:

- Verify applicable aviation, radio, location, and insurance requirements at test time.
- Use an appropriate small test platform, propeller protection where feasible, and a controlled test area.
- Keep people, animals, roads, structures, and unrelated property outside the operating area.
- Provide an independent human override and a tested hardware kill/disarm path that does not depend on the learned policy.
- Enforce conservative geofencing, attitude, altitude, velocity, battery, and link-loss limits outside the policy.
- Validate sensor calibration, command bounds, timing, and failsafe behavior with propellers removed first.
- Use staged tests: software-in-the-loop, hardware-in-the-loop, restrained/guarded tests, then limited free flight.
- Define abort criteria and assign one person responsibility for safety and one for operation when appropriate.
- Preserve logs for both successful and aborted tests.

## Prohibited shortcuts

- No autonomous test around people or in uncontrolled public spaces.
- No relying on the learned model as the sole safety mechanism.
- No disabling platform failsafes merely to improve a metric.
- No physical deployment based on a best-run video or a single seed.

The safety plan must be updated for the actual aircraft, location, and current regulations before real-world work begins.
