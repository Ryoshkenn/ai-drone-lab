# ADR 0001: Start with state-based hover in gym-pybullet-drones

- Status: proposed
- Date: 2026-09-20

## Context

The long-term idea includes FPV racing, vision, cross-simulator transfer, and possibly physical flight. Starting with all of those at once would make failures difficult to diagnose. The first experiment needs fast resets, headless execution, measurable state, and a known reference implementation.

## Decision

Begin with numerical kinematic observations and a hover task in `gym-pybullet-drones`. Use Stable-Baselines3 PPO as the reference learner before implementing a custom PPO loop. Treat Liftoff as a later transfer environment, not the primary trainer.

## Consequences

- The first milestone tests the training pipeline rather than visual perception.
- Existing physics and PPO code are dependencies, so “from scratch” applies to randomly initialized policy/value weights—not every software layer.
- A learned hover is necessary evidence, but it is not yet FPV racing or real-world autonomy.
- The simulator and default task must be audited before results are treated as owned experiments.

