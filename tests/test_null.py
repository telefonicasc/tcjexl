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


import unittest
from tcjexl import JEXL


class TestNull(unittest.TestCase):

    def setUp(self) -> None:
        self.jexl = JEXL()

    def test_null_fail(self):
        context = {"a": None}
        self.assertRaises(TypeError, self.jexl.evaluate, 'a*10', context)

    def test_nullsafe_number(self):
        expr = 'a|nullSafe(0)*10'
        context1 = {"a": None}
        context2 = {"a": 23}
        result1 = self.jexl.evaluate(expr, context1)
        result2 = self.jexl.evaluate(expr, context2)
        self.assertEqual(result1, 0)
        self.assertEqual(result2, 230)

    def test_nullsafe_string(self):
        expr = "a|nullSafe('foo')+'bar'"
        context1 = {"a": None}
        context2 = {"a": 'zzz'}
        result1 = self.jexl.evaluate(expr, context1)
        result2 = self.jexl.evaluate(expr, context2)
        self.assertEqual(result1, 'foobar')
        self.assertEqual(result2, 'zzzbar')

    def test_nullsafe_boolean(self):
        expr = "a|nullSafe(false)"
        context1 = {"a": None}
        context2 = {"a": True}
        result1 = self.jexl.evaluate(expr, context1)
        result2 = self.jexl.evaluate(expr, context2)
        self.assertEqual(result1, False)
        self.assertEqual(result2, True)

    def test_nullsafe_variable(self):
        expr = "a|nullSafe(b)"
        context1 = {"a": None, "b": 32}
        context2 = {"a": 4, "b": 32}
        result1 = self.jexl.evaluate(expr, context1)
        result2 = self.jexl.evaluate(expr, context2)
        self.assertEqual(result1, 32)
        self.assertEqual(result2, 4)
