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
# - currentTime
# - currentTimeIso
# - toIsoString
# - currentTimeFormat
# - timeFormat
# - currentHour24
# - currentDay

import unittest
import datetime
from tcjexl import JEXL

class TestTransformsDate(unittest.TestCase):

    def setUp(self) -> None:
        # Fixed time to 2024-02-01T12:43:55.123Z
        def test_now():
            return datetime.datetime(2024, 2, 1, 12, 43, 55, 123, tzinfo=datetime.timezone.utc)

        self.jexl = JEXL(now=test_now)

    def test_currentTime(self):
        result = self.jexl.evaluate('0|currentTime', {})
        self.assertEqual(result, datetime.datetime(2024, 2, 1, 12, 43, 55, 123, tzinfo=datetime.timezone.utc))

    def test_currentTimeIso(self):
        result = self.jexl.evaluate('0|currentTimeIso', {})
        self.assertEqual(result, '2024-02-01T12:43:55.000Z')

    def test_toIsoString(self):
        result = self.jexl.evaluate('0|currentTime|toIsoString', {})
        self.assertEqual(result, '2024-02-01T12:43:55.000Z')

    def test_currentTimeFormat(self):
        result = self.jexl.evaluate("0|currentTimeFormat('%Y')", {})
        self.assertEqual(result, '2024')

    def test_timeFormat(self):
        result = self.jexl.evaluate("0|currentTime|timeFormat('%Y')", {})
        self.assertEqual(result, '2024')

    def test_currentHour24(self):
        result = self.jexl.evaluate('0|currentHour24', {})
        self.assertEqual(result, 12)

    def test_currentDay(self):
        result = self.jexl.evaluate('0|currentDay', {})
        self.assertEqual(result, 1)


