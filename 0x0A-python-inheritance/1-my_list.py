#!/usr/bin/python3
"""class module"""


class MyList(list):
    """list class"""

    def print_sorted(self):
        """prints list sorted in ascendind order"""

        rtn = self.copy()
        rtn.sort(reverse=False)
        print(rtn)
