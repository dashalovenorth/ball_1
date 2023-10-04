from math import pi


def degree(tim, accel, rad, vel: float = 0) -> float:
    way = vel * tim + (accel * (tim ** 2)) / 2
    lgth = 2 * pi * rad
    radius_1 = (way / lgth).__round__(2)

    return radius_1


print(degree(1, 4, 7, 9))
