from vector import Vector

v = Vector(3, 4)
v2 = Vector(1, 2)


def test_norm():
    assert v.norm == 5


def test_access():
    assert v.x == 3
    assert v.y == 4


def test_product():
    assert v.scalar(v2) == 11