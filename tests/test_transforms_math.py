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
# - rnd
# - rndFloat
# - round
# - floor
# - parseInt
# - parseFloat

import unittest
from tcjexl import JEXL

class TestTransformsMath(unittest.TestCase):

    def setUp(self) -> None:
        self.jexl = JEXL()

    def test_rnd(self):
        result = self.jexl.evaluate('0|rnd(10)', {})
        self.assertGreaterEqual(result, 0)
        self.assertLess(result, 10)

    def test_rndFloat(self):
        result = self.jexl.evaluate('0|rndFloat(10)', {})
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 10)

    def test_round(self):
        result = self.jexl.evaluate('4.7882|round(2)', {})
        self.assertEqual(result, 4.79)

    def test_floor(self):
        result = self.jexl.evaluate('4.9|floor', {})
        self.assertEqual(result, 4)

    def test_parseInt(self):
        context = {'v': '42'}
        result = self.jexl.evaluate('v|parseInt', context)
        self.assertEqual(result, 42)

    def test_parseFloat(self):
        context = {'v': '-32.567'}
        result = self.jexl.evaluate('v|parseFloat', context)
        self.assertEqual(result, -32.567)
