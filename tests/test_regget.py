#!/usr/bin/env python3
from unittest import TestCase

import regget
from regget import (
    first_group_or_none,
    all_groups_or_none,
)

class ReggetTest(TestCase):
    def test_first_group_or_none(self):
        for pattern, string, result in [
                ("hej", "", None),
                ("hej", "hej", None),
                ("h.j", "hej", None),
                ("CO", "CO", None),
                ("(CO)", "CO", "CO"),
                ("(..)", "CO", "CO"),
                ("A(\d+)B", "A43B", "43"),
                ("A(\d+)(B)", "A43B", "43"),
                ("(A)(\d+)(B)", "A43B", "A"),
            ]:
            self.assertEqual(first_group_or_none(pattern, string), result)
            
    def test_all_groups_or_none(self):
        for pattern, string, result in [
                ("hej", "hej", None),
                ("h.j", "hej", None),
                ("CO", "CO", None),
                ("(CO)", "CO", ("CO",)),
                ("(..)", "CO", ("CO",)),
                ("A(\d+)B", "A43B", ("43",)),
                ("A(\d+)(B)", "A43B", ("43", "B")),
                ("(A)(\d+)(B)", "A43B", ("A", "43", "B")),
                ("hej", "", None),
            ]:
            self.assertEqual(all_groups_or_none(pattern, string), result)
            
    def test_readme(self):
        from functools import partial
        PATTERN = "CO-(\d+)"
        grab_number = partial(regget.first_group_or_none, PATTERN)
        document_names = ["CO-3", "CO-9", "CO-12"]
        valid_numbers = [grab_number(s) for s in document_names]
        self.assertEqual(valid_numbers, ["3", "9", "12"])
