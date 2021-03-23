from vector import Vector
from math import pi
from math import sqrt

v = Vector(3, 4)
v2 = Vector(1, 2)
v3 = Vector(8, 0)
v4 = Vector(0, 8)
v5 = Vector(8, 8)
v6 = Vector(-8, 8)
v7 = Vector(-8, -8)
v8 = Vector(8, -8)
v9 = Vector(sqrt(3)/2, 1/2)
v10 = Vector(-sqrt(3)/2, 1/2)


def test_norm():
    assert v.norm == 5


def test_access():
    assert v.x == 3
    assert v.y == 4


def test_product():
    assert v.scalar(v2) == 11


def test_argument():
    assert v3.arg == 0
    assert v4.arg == pi/2
    assert round(v5.arg, 6)/pi == round(pi/4, 6)/pi
    assert round(v6.arg, 6)/pi == round(3*pi/4, 6)/pi
    assert round(v7.arg, 6)/pi == round(-3*pi/4, 6)/pi
    assert round(v8.arg, 6)/pi == round(-pi/4, 6)/pi
    assert round(v9.arg, 6)/pi == round(pi/6, 6)/pi
    assert round(v10.arg, 6)/pi == round(5*pi/6, 6)/pi









