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
# - next
# - indexOf
# - rndList
# - rndFloatList
# - zipStringList
# - concatList


import unittest
from tcjexl import JEXL

class TestTransformsList(unittest.TestCase):

    def setUp(self) -> None:
        self.jexl = JEXL()

    def test_next(self):
        result = self.jexl.evaluate('12|next([1,2,3,12,15,18])', {})
        self.assertEqual(result, 15)

    def test_indexOf(self):
        context = {'c': [1, 2, 3, 12, 15, 18]}
        result = self.jexl.evaluate('c|indexOf(15)', context)
        self.assertEqual(result, 4)

    def test_rndList(self):
        result = self.jexl.evaluate('0|rndList(6,8)', {})
        self.assertEqual(len(result), 8)
        for item in result:
            self.assertGreaterEqual(item, 0)
            self.assertLess(item, 6)

    def test_rndFloatList(self):
        result = self.jexl.evaluate('0|rndFloatList(6,8)', {})
        self.assertEqual(len(result), 8)
        for item in result:
            self.assertGreaterEqual(item, 0)
            self.assertLessEqual(item, 6)

    def test_zipStringList(self):
        context = {'x': ['a', 'b', 'c']}
        result = self.jexl.evaluate("x|zipStringList(['A', 'B', 'C'], '-')", context)
        self.assertEqual(result, ['a-A', 'b-B', 'c-C'])

        # Invalid usage (list size missmatch)
        self.assertRaises(ValueError, self.jexl.evaluate, "x|zipStringList(['A', 'B', 'C', 'D'], '-')", context)

    def test_concatList(self):
        context = {'x': ['a', 'bbbb', 'c']}
        result = self.jexl.evaluate('x|concatList', context)
        self.assertEqual(result, 'abbbbc')
