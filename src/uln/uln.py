from functools import total_ordering
from .uln_validator import ULNValidator


@total_ordering
class ULN:
    """
    Represents a 10-digit Unique Learner Number (ULN).

    See: https://www.gov.uk/education/learning-records-service-lrs
    """

    def __init__(self, value: str):
        self._value = ULNValidator.require_valid_uln(value)

    @classmethod
    def from_string(cls, value: str) -> 'ULN':
        """
        Creates a new ULN object from the specified string value.

        :param value: the ULN value as a string
        :return: a ULN object
        """
        return cls(value)

    def __eq__(self, other):
        if not isinstance(other, ULN):
            return NotImplemented
        return self._value == other._value

    def __lt__(self, other):
        if not isinstance(other, ULN):
            return NotImplemented
        return self._value < other._value

    def __hash__(self):
        return hash(self._value)

    def __str__(self):
        return f"ULN({self._value})"

    def __repr__(self):
        return self.__str__()
