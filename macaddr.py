from typing import Optional
import re
from itertools import islice
from functools import lru_cache

__all__ = ['MacAddress']


class MacAddress(object):
    _mac_char_re = re.compile(r"[0-9a-f]", re.I)

    def __init__(self, macaddr: str):
        self.chars = self._mac_char_re.findall(macaddr)
        if len(self.chars) != 12:
            raise ValueError(f"Invalid MAC address: {macaddr}")

    @lru_cache
    def format(
        self,
        size: Optional[int] = 2,
        sep: Optional[str] = ":",
        uppercase: Optional[bool] = False,
    ):
        i_chars = iter(self.chars)
        chunks, rem = divmod(12, size)

        if rem != 0:
            raise ValueError(f"Invalid size {size}, not divisible from 12")

        value = sep.join(["".join(islice(i_chars, size)) for _ in range(chunks)])
        return value if not uppercase else value.upper()

    def __repr__(self):
        return f"{self.__class__.__name__}({str(self)})"

    def __str__(self):
        return self.format()
