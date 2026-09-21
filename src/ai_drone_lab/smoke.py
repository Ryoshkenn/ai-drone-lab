"""Headless integration smoke test for the pinned drone simulator."""

from __future__ import annotations

import argparse
import contextlib
import importlib.metadata
import io
import platform
import sys
from typing import Any

import gym_pybullet_drones
import numpy as np
from gym_pybullet_drones.envs.HoverAviary import HoverAviary
from gym_pybullet_drones.utils.enums import ActionType, ObservationType

from ai_drone_lab.summary import canonical_json, observation_digest


def _space_summary(space: Any) -> dict[str, Any]:
    """Describe a Gymnasium Box without dumping every bound."""
    high_max = float(np.max(space.high))
    low_min = float(np.min(space.low))
    return {
        "dtype": str(space.dtype),
        "high_max": high_max if np.isfinite(high_max) else None,
        "low_min": low_min if np.isfinite(low_min) else None,
        "shape": list(space.shape),
    }


def run_smoke(*, steps: int, seed: int) -> dict[str, Any]:
    """Step a seeded environment with seeded random actions and summarize the run."""
    if steps < 1:
        raise ValueError("steps must be at least 1")

    # The upstream constructor prints URDF details. Keep stdout reserved for JSON.
    with contextlib.redirect_stdout(io.StringIO()):
        environment = HoverAviary(gui=False, obs=ObservationType.KIN, act=ActionType.RPM)
    try:
        observation, _ = environment.reset(seed=seed)
        initial_digest = observation_digest(observation)
        rng = np.random.default_rng(seed)
        terminated = False
        truncated = False
        executed_steps = 0
        total_reward = 0.0

        for _ in range(steps):
            action = rng.uniform(
                low=environment.action_space.low,
                high=environment.action_space.high,
                size=environment.action_space.shape,
            ).astype(environment.action_space.dtype)
            observation, reward, terminated, truncated, _ = environment.step(action)
            executed_steps += 1
            total_reward += float(reward)
            if terminated or truncated:
                break

        return {
            "action_space": _space_summary(environment.action_space),
            "executed_steps": executed_steps,
            "final_observation_digest": observation_digest(observation),
            "initial_observation_digest": initial_digest,
            "observation_space": _space_summary(environment.observation_space),
            "platform": platform.platform(),
            "python": sys.version.split()[0],
            "requested_steps": steps,
            "seed": seed,
            "simulator": gym_pybullet_drones.__name__,
            "simulator_version": importlib.metadata.version("gym-pybullet-drones"),
            "terminated": bool(terminated),
            "total_reward": round(total_reward, 8),
            "truncated": bool(truncated),
        }
    finally:
        environment.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--steps", type=int, default=30)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    print(canonical_json(run_smoke(steps=args.steps, seed=args.seed)), end="")


if __name__ == "__main__":
    main()
