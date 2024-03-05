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
# - strToLocation
# - typeOf

import unittest
from tcjexl import JEXL

class TestTransformsMisc(unittest.TestCase):

    def setUp(self) -> None:
        self.jexl = JEXL()


    def test_typeOf(self):
        context = {"a": "text", "b": 7, "c": 7.4, "d": True, "e": None, "f": {}, "g": []}
        result = self.jexl.evaluate('a|typeOf', context)
        self.assertEqual(result, 'str')
        result = self.jexl.evaluate('b|typeOf', context)
        self.assertEqual(result, 'int')
        result = self.jexl.evaluate('c|typeOf', context)
        self.assertEqual(result, 'float')
        result = self.jexl.evaluate('d|typeOf', context)
        self.assertEqual(result, 'bool')
        result = self.jexl.evaluate('e|typeOf', context)
        self.assertEqual(result, 'NoneType')
        result = self.jexl.evaluate('f|typeOf', context)
        self.assertEqual(result, 'dict')
        result = self.jexl.evaluate('g|typeOf', context)
        self.assertEqual(result, 'list')

    def test_strToLocation(self):
        result = self.jexl.evaluate('"-10.13,24.54"|strToLocation', {})
        self.assertEqual(result, [-10.13, 24.54])
