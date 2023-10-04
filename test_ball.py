import pytest
from ball import degree

test_degree = [
      (12, 5, 4, 7, 17.67),
      (36, 9, 7, 13, 143.24),
      (17, 4, 9, 6, 12.03),
]


@pytest.mark.parametrize('tim, accel, rad, vel, expected', test_degree)
def test_degree_1(tim, accel, rad, vel: float, expected: float) -> None:
    assert degree(tim, accel, rad, vel) == expected
