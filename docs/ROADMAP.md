# Roadmap and quality gates

This roadmap is sequential. A later phase may be researched early, but it is not considered active until the previous gate has passed.

## Phase 0 — Reproducible baseline

### Work

- Pin a compatible Python and simulator revision.
- Run the simulator headlessly and record a deterministic smoke-test summary.
- Reproduce the upstream PPO hover example without modifying its reward.
- Benchmark simulation steps per second on the available laptop.
- Establish the experiment manifest and logbook workflow.

### Exit gate

- A fresh checkout can run lint, unit tests, and the smoke test from documented commands.
- At least two reruns with the same seed produce matching initial observation and termination summaries on the same machine.
- The reference PPO command, wall-clock time, configuration, and evaluation metrics are recorded.
- Failures and deviations from upstream behavior are documented.

## Phase 1 — Owned hover experiment

### Work

- Define an observation vector and document every element and unit.
- Choose an action abstraction. Compare direct motor RPM control with a rate/thrust abstraction before claiming FPV relevance.
- Implement an owned hover environment, reward, termination rules, and evaluation harness.
- Train a Stable-Baselines3 PPO reference policy from random initialization.
- Evaluate across multiple training seeds and held-out initial states.

### Provisional exit gate

The exact thresholds become final after the untrained and conventional-controller baselines are measured. The initial target is:

- five independently trained seeds;
- 100 held-out episodes per seed;
- at least 90% of episodes complete 10 seconds without a crash or boundary violation;
- median position RMSE at most 0.25 m;
- report median, interquartile range, worst seed, and representative failures.

Passing one favorable seed is not sufficient.

## Phase 2 — Target navigation

- Randomize the target and initial conditions.
- Add time-to-target, overshoot, path efficiency, and collision metrics.
- Hold out spatial regions and disturbance settings during training.
- Compare against a conventional PID reference where the comparison is meaningful.

## Phase 3 — Gate navigation

- Define gates and ordered traversal semantics.
- Train on procedurally varied layouts.
- Evaluate on fixed, versioned, unseen courses.
- Report completion rate, clean gate passages, collisions, and lap time.

## Phase 4 — FPV vision

- Replace privileged state with camera observations in controlled increments.
- Profile data generation and accelerator use before scaling hardware.
- Compare end-to-end vision with a modular perception-plus-control baseline.
- Document frame rate, latency, image transformations, and domain randomization.

## Phase 5 — Cross-simulator transfer

- Treat Liftoff telemetry/controller integration as a separate engineering investigation.
- Freeze the source-simulator model before held-out transfer evaluation.
- Record any adapter, calibration, or fine-tuning used.
- Never label fine-tuned transfer as zero-shot transfer.

## Phase 6 — Physical platform

This phase requires a new, explicit decision record. It cannot begin merely because a simulated policy looks convincing. See [SAFETY.md](SAFETY.md).

## Definition of done for every experiment

- The question and hypothesis were written before interpreting results.
- Configuration, seed set, code revision, and environment are recoverable.
- Baselines and evaluation protocol are stated.
- Aggregate results and failures are retained.
- The conclusion says what the evidence supports and what it does not.

