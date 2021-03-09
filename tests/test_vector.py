from vector import Vector
from math import pi, sqrt

v = Vector(3, 4)
v2 = Vector(1, 2)
v3 = Vector(1, 0)
v4 = Vector(0, 1)
v5 = Vector(-1, 0)
v6 = Vector(1, 1)
v7 = Vector(1, -1)
v8 = Vector(-1, 1)
v9 = Vector(-1, -1)
v10 = Vector(0, 0)


def test_norm():
    assert v.norm == 5


def test_argument():
    assert v3.arg == 0
    assert v4.arg == pi / 2.
    assert v5.arg == pi
    assert round(v6.arg, 6) == round(pi / 4, 6)
    assert round(v7.arg, 6) == -round(pi / 4, 6)
    assert round(v8.arg, 6) == round(3 * pi / 4, 6)
    assert round(v9.arg, 6) == -round(3 * pi / 4, 6)
    assert v10 is None


def test_access():
    assert v.x == 3
    assert v.y == 4


def test_product():
    assert v.scalar(v2) == 11
