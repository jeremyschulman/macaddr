from typing import Optional, Callable
import re
from itertools import islice
from functools import lru_cache

__all__ = ["MacAddress"]


class MacAddress(object):
    """
    MacAddress allows a Caller to declare an instance of a network MAC address string
    value so that future calls to the `format` method will result is differnet format
    groupings.  Common formats are:

        size=4, sep='.' => AABB.CCDD.EEFF
        size=2, sep=':' => AA:BB:CC:DD:EE:FF
        size=3, sep='-' => AAB-BDD-DDE-EFF

    The `format` settings/return value are cached so that future calls using the
    same format criteria are optimized.  This is a desired condition since the
    MAC address format value may be used multiple times across many usages; for
    example when looking for a MAC address in multiple network devices.
    """

    _mac_char_re = re.compile(r"[0-9a-f]", re.I)

    def __init__(self, macaddr: str):
        """
        Initializes the MacAddress instance with a given MAC string value, of
        any format and character case.  The Caller can then use the `format`
        method to return back any desired format.

        Parameters
        ----------
        macaddr: str - The initial MAC address string

        Raises
        ------
        ValueError - when the provided MAC address is not 12 characters in
        length; not counting any of the octet-group separators.
        """
        self.chars = self._mac_char_re.findall(macaddr)
        if len(self.chars) != 12:
            raise ValueError(f"Invalid MAC address: {macaddr}")

    @lru_cache
    def format(
        self,
        size: Optional[int] = 2,
        sep: Optional[str] = ":",
        to_case: Optional[Callable] = None,
    ):
        """
        Format the MAC address to the defined group size and group separator.  The default
        settings of size=2 and sep=":" result in a MAC address format in "AA:BB:CC:DD:EE:FF"
        notation, for example.

        The Caller can also use the `to_case` parameter to return the value
        using str.lower or str.upper case.  By default if `to_case` is not
        provided, then the character casing will be "as-is" passed in the
        instance constructor.

        The format settings/return value are cached so that future calls using
        the same format criteria are optimized.  This is a desired condition
        since the MAC address format value may be used multiple times across
        many usages; for example when looking for a MAC address in multiple
        network devices.

        Parameters
        ----------
        size: int - The group size of the octets.
        sep: char - The group separator.
        to_case: Callable - should generally be str.lower or str.upper for case formatting

        Returns
        -------
        str - the formatted MAC address string.

        Raises
        ------
        ValueError if `size` value is not divisible by 12; number characters in
        a MAC address not counting the group separator character.
        """
        i_chars = iter(self.chars)
        chunks, rem = divmod(12, size)

        if rem != 0:
            raise ValueError(f"Invalid size {size}, not divisible from 12")

        value = sep.join("".join(islice(i_chars, size)) for _ in range(chunks))
        return value if not to_case else to_case(value)

    def __repr__(self):
        return f"{self.__class__.__name__}({str(self)})"

    def __str__(self):
        return self.format()
