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


import pyjexl
import random
import datetime
import math
import functools

from datetime import timezone
from .expression_functions import linearInterpolator, linearSelector, randomLinearInterpolator, zipStrList, valueResolver

class JEXL(pyjexl.JEXL):
    def __init__(self, context=None, now=datetime.datetime.now(timezone.utc)):
        super().__init__(context=context)

        self.now = now

        # Tested by test_transforms_math.py
        super().add_transform("rnd", lambda ini, end: random.randrange(ini, end))
        super().add_transform("rndFloat", lambda ini, end: random.uniform(ini, end))
        super().add_transform("round", lambda x, decimals: round(x, decimals))
        super().add_transform("floor", lambda x: math.floor(x))
        super().add_transform("parseInt", lambda x: int(x))
        super().add_transform("parseFloat", lambda x: float(x))

        # Tested by test_transforms_string.py
        super().add_transform("uppercase", lambda x: str(x).upper())
        super().add_transform("lowercase", lambda x: str(x).lower())
        super().add_transform("toString", lambda x: str(x))
        super().add_transform("substring", lambda x, ini, fin: x[ini:fin])
        super().add_transform("includes", lambda x, str: str in x)
        super().add_transform("len", lambda data: len(data))

        # Tested by test_transforms_list.py
        super().add_transform("next", lambda x, arr: arr[(arr.index(x) + 1) % len(arr)])
        super().add_transform("indexOf", lambda x, str: x.index(str))
        super().add_transform("rndList", lambda init, end, length: [random.randrange(init, end) for _ in range(length)])
        super().add_transform("rndFloatList", lambda ini, end, length: [random.uniform(ini, end) for _ in range(length)])
        super().add_transform("zipStringList", zipStrList)
        super().add_transform("concatList", lambda list_value: functools.reduce(lambda a, b: a + b, list_value))

        # Tested by test_transforms_date.py
        super().add_transform("currentTime", lambda x: self.now())
        super().add_transform("currentTimeIso", lambda x: self.now().strftime('%Y-%m-%dT%H:%M:%S') + ".000Z")
        super().add_transform("toIsoString", lambda date: date.strftime('%Y-%m-%dT%H:%M:%S') + ".000Z")
        super().add_transform("currentTimeFormat", lambda x, string: self.now().strftime(string))
        super().add_transform("timeFormat", lambda date, string: date.strftime(string))
        super().add_transform("currentHour24", lambda x: int(self.now().hour))
        super().add_transform("currentDay", lambda x: int(self.now().day))

        # Tested by test_transforms_interpolation.py
        super().add_transform("interpolate", lambda step, ini, end, nSteps: ((end - ini) * (step % nSteps)) / nSteps)
        super().add_transform("linearInterpolator", lambda t, array: linearInterpolator(t, array))
        super().add_transform("linearSelector", lambda t, array: linearSelector(t, array))
        super().add_transform("randomLinearInterpolator", lambda t, rndFactor, array: randomLinearInterpolator(t, rndFactor, array))
        super().add_transform("alertMaxValue", lambda value, max_value: True if value >= max_value else False)
        super().add_transform("valueResolver", lambda t, values: valueResolver(t, values))

        # Tested by test_transforms_misc.py
        super().add_transform("typeOf", lambda x: f'{type(x)}'[8:-2])
        super().add_transform("strToLocation", lambda str: [float(x) for x in str.split(",")])
