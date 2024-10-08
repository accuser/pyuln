import re
from typing import Union


class ULNValidator:
    """
    Utility class for validating a ULN (Unique Learner Number) value.
    """

    _ULN_REGEX = re.compile(r'^(?P<digits>\d{9})(?P<check_digit>\d{1})$')

    @classmethod
    def require_valid_uln(cls, value: Union[str, 'ULN']) -> str:
        """
        Validates the specified ULN value.

        :param value: the ULN value to validate
        :return: the specified ULN value
        :raises ValueError: if the specified ULN value is invalid
        """
        if hasattr(value, '_value'):  # Check if it's a ULN object
            return value._value
        if not isinstance(value, str):
            raise TypeError("ULN value must be a string")
        if not cls.is_valid_uln(value):
            raise ValueError("Invalid ULN value")
        return value

    @classmethod
    def is_valid_uln(cls, value: str) -> bool:
        """
        Validates the format of the specified ULN value.

        :param value: the ULN value to validate
        :return: True if the specified ULN value is valid; False otherwise
        :raises ValueError: if the specified ULN value has an invalid format
        """
        match = cls._ULN_REGEX.match(value)
        if not match:
            raise ValueError("Invalid ULN format")

        digits = match.group("digits")
        check_digit = int(match.group("check_digit"))

        remainder = cls._calculate_sum(digits) % 11

        if remainder == 0:
            return False

        return (10 - remainder) == check_digit

    @staticmethod
    def _calculate_sum(digits: str) -> int:
        """
        Calculates the sum of the ULN digits based on the specified formula.

        :param digits: the digits of the ULN value
        :return: the sum of the ULN digits
        """
        return sum((10 - i) * int(digit) for i, digit in enumerate(digits))
