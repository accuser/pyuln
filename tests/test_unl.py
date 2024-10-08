import unittest
from uln import ULN

class TestULN(unittest.TestCase):
    def test_uln_from_string(self):
        uln = ULN.from_string("0000000042")
        self.assertIsInstance(uln, ULN)

    def test_uln_from_string_with_invalid_value(self):
        with self.assertRaises(ValueError):
            ULN.from_string("0000000000")

    def test_uln_equality(self):
        uln1 = ULN.from_string("0000000042")
        uln2 = ULN.from_string("0000000042")
        uln3 = ULN.from_string("0000000050")
        self.assertEqual(uln1, uln2)
        self.assertNotEqual(uln1, uln3)

    def test_uln_comparison(self):
        uln1 = ULN.from_string("0000000042")
        uln2 = ULN.from_string("0000000050")
        self.assertLess(uln1, uln2)
        self.assertGreater(uln2, uln1)

    def test_uln_hash(self):
        uln1 = ULN.from_string("0000000042")
        uln2 = ULN.from_string("0000000042")
        self.assertEqual(hash(uln1), hash(uln2))

    def test_uln_str(self):
        uln = ULN.from_string("0000000042")
        self.assertEqual(str(uln), "ULN(0000000042)")


if __name__ == '__main__':
    unittest.main()