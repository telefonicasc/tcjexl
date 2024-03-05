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
# - interpolate
# - linearInterpolator
# - linearSelector
# - randomLinearInterpolator
# - alertMaxValue
# - valueResolver

import unittest
from tcjexl import JEXL

class TestTransformsInterpolation(unittest.TestCase):

    def setUp(self) -> None:
        self.jexl = JEXL()

    def test_interpolate(self):
        result = self.jexl.evaluate('3|interpolate(0,10,9)', {})
        self.assertEqual(result, 10/3)

    def test_linearInterpolator(self):
        expr = 'linearInterpolator([[0, 0], [1, 1], [2, 1.5], [8, 1.8], [10, 2.0]])'
        result = self.jexl.evaluate('2|' + expr, {})
        self.assertEqual(result, 1.5)
        result = self.jexl.evaluate('5|' + expr, {})
        self.assertEqual(result, 1.65)

        # Invalid usage (interpolation out of range)
        self.assertRaises(ValueError, self.jexl.evaluate, '11|' + expr, {})

    def test_linearSelector(self):
        expr = 'linearSelector([[0.02, "BLACK"], [0.04, "NO FLAG"], [0.06, "RED"], [0.21, "YELLOW"], [1, "GREEN"]])'
        result = self.jexl.evaluate('0.01|' + expr, {})
        self.assertEqual(result, 'BLACK')
        result = self.jexl.evaluate('0.03|' + expr, {})
        self.assertEqual(result, 'NO FLAG')
        result = self.jexl.evaluate('0.05|' + expr, {})
        self.assertEqual(result, 'RED')
        result = self.jexl.evaluate('0.07|' + expr, {})
        self.assertEqual(result, 'YELLOW')
        result = self.jexl.evaluate('0.25|' + expr, {})
        self.assertEqual(result, 'GREEN')

        # Invalid usage (interpolation out of range)
        self.assertRaises(ValueError, self.jexl.evaluate, '2|' + expr, {})


    def test_randomLinearInterpolator(self):
        expr = 'randomLinearInterpolator([0.85, 0.99], [[0, 0], [1, 1], [2, 1.5], [8, 1.8], [10, 2.0]])'
        result = self.jexl.evaluate('2|' + expr, {})
        self.assertGreaterEqual(result, 1.5*0.85)
        self.assertLessEqual(result, 1.5*0.99)
        result = self.jexl.evaluate('5|' + expr, {})
        self.assertGreaterEqual(result, 1.65*0.85)
        self.assertLessEqual(result, 1.65*0.99)

        # Invalid usage (interpolation out of range)
        self.assertRaises(ValueError, self.jexl.evaluate, '11|' + expr, {})

    def test_alertMaxValue(self):
        expr = 'alertMaxValue(2)'
        result = self.jexl.evaluate('2.5|' + expr, {})
        self.assertEqual(result, True)
        result = self.jexl.evaluate('2|' + expr, {})
        self.assertEqual(result, True)
        result = self.jexl.evaluate('1.5|' + expr, {})
        self.assertEqual(result, False)

    def test_valueResolver(self):
        expr = 'valueResolver([["BLACK", "stormy"], ["NO FLAG", "curly"], ["RED", "stormy"], ["YELLOW", "curly"], ["GREEN", "plain"]])'
        result = self.jexl.evaluate('"BLACK"|' + expr, {})
        self.assertEqual(result, 'stormy')
        result = self.jexl.evaluate('"NO FLAG"|' + expr, {})
        self.assertEqual(result, 'curly')
        result = self.jexl.evaluate('"RED"|' + expr, {})
        self.assertEqual(result, 'stormy')
        result = self.jexl.evaluate('"YELLOW"|' + expr, {})
        self.assertEqual(result, 'curly')
        result = self.jexl.evaluate('"GREEN"|' + expr, {})
        self.assertEqual(result, 'plain')

        # Invalid usage (unknown value)
        self.assertRaises(ValueError, self.jexl.evaluate, '"UNKNOWN"|' + expr, {})
