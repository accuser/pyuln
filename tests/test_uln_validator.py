import unittest
from uln import ULN, ULNValidator


class TestULNValidator(unittest.TestCase):
    def test_require_valid_uln_with_valid_string(self):
        result = ULNValidator.require_valid_uln("0000000042")
        self.assertEqual(result, "0000000042")

    def test_require_valid_uln_with_invalid_string(self):
        with self.assertRaises(ValueError):
            ULNValidator.require_valid_uln("0000000000")

    def test_require_valid_uln_with_uln_object(self):
        uln = ULN.from_string("0000000042")
        result = ULNValidator.require_valid_uln(uln)
        self.assertEqual(result, "0000000042")

    def test_is_valid_uln_with_valid_string(self):
        self.assertTrue(ULNValidator.is_valid_uln("0000000042"))

    def test_is_valid_uln_with_invalid_string(self):
        self.assertFalse(ULNValidator.is_valid_uln("0000000000"))


if __name__ == '__main__':
    unittest.main()
