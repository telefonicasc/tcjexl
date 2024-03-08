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


class TestContextAsArgument(unittest.TestCase):

    def test_context_as_argument(self):
        jexl = JEXL()

        context1 = {"haystack": "long string", "needle": "long"}
        context2 = {"haystack": "long string", "needle": "short"}
        expression = 'haystack|includes(needle)'

        result = jexl.evaluate(expression, context1)
        self.assertEqual(result, True)

        result = jexl.evaluate(expression, context2)
        self.assertEqual(result, False)
