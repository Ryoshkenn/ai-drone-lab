"""Small, dependency-light helpers for reproducible experiment summaries."""

from __future__ import annotations

import hashlib
import json
from typing import Any

import numpy as np


def observation_digest(observation: np.ndarray) -> str:
    """Return a stable short digest for an observation array."""
    contiguous = np.ascontiguousarray(observation)
    metadata = f"{contiguous.dtype.str}:{contiguous.shape}".encode()
    return hashlib.sha256(metadata + contiguous.tobytes()).hexdigest()[:16]


def canonical_json(data: dict[str, Any]) -> str:
    """Serialize a summary consistently for comparison and version control."""
    return json.dumps(data, indent=2, sort_keys=True) + "\n"

