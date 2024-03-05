# Copyright 2024 Telefónica Soluciones de Informática y Comunicaciones de España, S.A.U.
#
# This file is part of tcjexl
#
# tcjexl is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# tcjexl is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with IoT orchestrator. If not, see http://www.gnu.org/licenses/.

# This file tests the following transformations:
#
# - uppercase
# - lowercase
# - toString
# - substring
# - includes
# - len

import unittest
from tcjexl import JEXL


class TestTransformsString(unittest.TestCase):

    def setUp(self) -> None:
        self.jexl = JEXL()

    def test_uppercase(self):
        context = {'c': 'aGivenString'}
        result = self.jexl.evaluate('c|uppercase', context)
        self.assertEqual(result, 'AGIVENSTRING')

    def test_lowercase(self):
        context = {'c': 'aGivenString'}
        result = self.jexl.evaluate('c|lowercase', context)
        self.assertEqual(result, 'agivenstring')

    def test_toString(self):
        context = {'c': ['ZZZ', {'x': 1, 'y': 2}]}
        result = self.jexl.evaluate('c|toString', context)
        self.assertEqual(result, "['ZZZ', {'x': 1, 'y': 2}]")

    def test_substring(self):
        context = {'c': 'aGivenString'}
        result = self.jexl.evaluate('c|substring(3,6)', context)
        self.assertEqual(result, 'ven')

    def test_includes(self):
        context = {'c': 'aGivenString'}
        result = self.jexl.evaluate('c|includes("Given")', context)
        self.assertEqual(result, True)
        result = self.jexl.evaluate('c|includes("Text")', context)
        self.assertEqual(result, False)

    def test_len(self):
        context = {'a': 'atext', 'b': [0, 1, 2]}
        result = self.jexl.evaluate('a|len', context)
        self.assertEqual(result, 5)
        result = self.jexl.evaluate('b|len', context)
        self.assertEqual(result, 3)
