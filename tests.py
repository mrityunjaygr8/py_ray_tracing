from unittest import TestCase, main
from vector import Vector


class Test_Vector(TestCase):
    def setUp(self):
        self.v = Vector(1, -2, -2)
        self.v2 = Vector(3, 6, 9)

    def test_represent(self):
        self.assertEqual(repr(self.v), "[1.0, -2.0, -2.0]")

    def test_magnitude(self):
        self.assertEqual(self.v.magnitude(), 3.0)

    def test_normalized(self):
        self.assertEqual(repr(self.v.normalized()), "[0.333, -0.667, -0.667]")

    def test_dot(self):
        self.assertEqual(self.v.dot(self.v2), -27.0)

    def test_add(self):
        self.assertEqual(repr(self.v + self.v2), "[4.0, 4.0, 7.0]")

    def test_sub(self):
        self.assertEqual(repr(self.v - self.v2), "[-2.0, -8.0, -11.0]")

    def test_mul(self):
        self.assertEqual(repr(self.v * 3), "[3.0, -6.0, -6.0]")

    def test_mul_wrong(self):
        with self.assertRaises(AssertionError):
            self.v * "a"

    def test_rmul(self):
        self.assertEqual(repr(3 * self.v), "[3.0, -6.0, -6.0]")

    def test_rmul_wrong(self):
        with self.assertRaises(AssertionError):
            "a" * self.v

    def test_div(self):
        self.assertEqual(repr(self.v2 / 3), "[1.0, 2.0, 3.0]")

    def test_div_wrong(self):
        with self.assertRaises(AssertionError):
            self.v2 / "a"

    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.v2 / 0


if __name__ == "__main__":
    main()
