import numpy as np

from neuroflight.smoke import _space_summary
from neuroflight.summary import canonical_json, observation_digest


def test_observation_digest_is_stable() -> None:
    observation = np.array([[1.0, 2.0, 3.0]], dtype=np.float32)

    assert observation_digest(observation) == observation_digest(observation.copy())


def test_observation_digest_includes_dtype() -> None:
    float32 = np.array([1.0, 2.0], dtype=np.float32)
    float64 = float32.astype(np.float64)

    assert observation_digest(float32) != observation_digest(float64)


def test_canonical_json_is_sorted_and_terminated() -> None:
    assert canonical_json({"z": 1, "a": 2}) == '{\n  "a": 2,\n  "z": 1\n}\n'


def test_space_summary_is_compact() -> None:
    class Space:
        dtype = np.dtype("float32")
        high = np.array([1.0, 2.0])
        low = np.array([-1.0, -2.0])
        shape = (2,)

    assert _space_summary(Space()) == {
        "dtype": "float32",
        "high_max": 2.0,
        "low_min": -2.0,
        "shape": [2],
    }
