from vector import Vector
from math import pi
import pytest
import math

v10 = Vector(0, 0)
v3 = Vector(1, 0)
v4 = Vector(0, 1)
v5 = Vector(-1, 0)
v11 = Vector(0, -1)
v6 = Vector(1, 1)
v8 = Vector(-1, 1)
v9 = Vector(-1, -1)
v7 = Vector(1, -1)
v2 = Vector(1, 2)
v = Vector(3, 4)


def test_norm():
    assert v.norm == 5


def test_argument():
    assert v10.arg is None
    assert v3.arg == 0
    assert v4.arg == pi / 2.0
    assert v5.arg == pi
    assert v11.arg == -pi / 2.0
    assert round(v6.arg, 6) == round(pi / 4, 6)
    assert round(v8.arg, 6) == round(3 * pi / 4, 6)
    assert round(v9.arg, 6) == -round(3 * pi / 4, 6)
    assert round(v7.arg, 6) == -round(pi / 4, 6)


def test_access():
    assert v.x == 3
    assert v.y == 4


def test_product():
    assert v.scalar(v2) == 11


@pytest.mark.parametrize("value, expected", [(v2, TypeError()), (3, Vector(9, 12))])
def test_mul(value, expected):
    if isinstance(expected, Exception):
        with pytest.raises(type(expected)):
            _ = v * value
    else:
        assert v * value == expected


def test_add_and_equal():
    assert v + v2 == Vector(4, 6)


def test_sub():
    assert v - v2 == Vector(2, 2)


@pytest.mark.parametrize(
    "theta, expected", [(0, v), (pi, Vector(-v.x, -v.y)), (2 * pi, v), (pi / 2.0, Vector(-v.y, v.x))]
)
def test_rotate(theta, expected):
    rot = v.rotate(theta)
    print(theta, v, expected, rot)
    assert rot == expected


def test_neg():
    assert -v == Vector(-3, -4)


def test_pos():
    assert +v == v


@pytest.mark.parametrize("value, expected", [(v2, TypeError()), (3, Vector(9, 12))])
def test_mul(value, expected):
    if isinstance(expected, Exception):
        with pytest.raises(type(expected)):
            _ = value * v
    else:
        assert value * v == expected


def test_iadd():
    a = Vector(v)
    a += v2
    assert a == Vector(4, 6)


def test_isub():
    a = Vector(v)
    a -= v2
    assert a == Vector(2, 2)


def test_imul():
    a = Vector(v)
    a *= 2
    assert a == Vector(6, 8)


def test_exp():
    assert Vector(118.73187487146112, 133.57251698701884) == math.exp(v)
