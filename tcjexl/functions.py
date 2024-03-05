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

import random

def zipStrList(left: list, right: list, sep: str = ""):
    l_length = len(left)
    r_length = len(right)
    if l_length == r_length:
        return [str(left[i]) + sep + str(right[i]) for i in range(l_length)]
    else:
        raise ValueError(f"zipStrList input error, left length: {l_length}, right len length: {r_length}")


def linearInterpolator(t, interpolations):
    def interpolate(start, end, t):
        return start + (end - start) * t

    for i in range(len(interpolations)):
        if i < len(interpolations) - 1 and interpolations[i][0] <= t < interpolations[i + 1][0]:
            start_time, start_value = interpolations[i]
            end_time, end_value = interpolations[i + 1]
            time_ratio = (t - start_time) / (end_time - start_time)
            return interpolate(start_value, end_value, time_ratio)

    raise ValueError("Invalid input or interpolations")


def valueResolver(t: str, elements: list):
    dictionary = {}
    for k, v in elements:
        dictionary[k] = v
    r = dictionary.get(t, None)
    if r is None:
        raise ValueError(f"Invalid key {t}")
    return r


def linearSelector(t, interpolations):
    for i in range(len(interpolations)):
        if t <= interpolations[i][0]:
            _, start_value = interpolations[i]
            return start_value

    raise ValueError("Invalid input or interpolations")


def randomLinearInterpolator(t, rndFactor, interpolations):
    def interpolate(start, end, t):
        return start + (end - start) * t

    def random_interpolate(start, end, t):
        random_value = random.uniform(rndFactor[0], rndFactor[1])
        return interpolate(start, end, t) * random_value

    for i in range(len(interpolations)):
        if i < len(interpolations) - 1 and interpolations[i][0] <= t < interpolations[i + 1][0]:
            start_time, start_value = interpolations[i]
            end_time, end_value = interpolations[i + 1]
            time_ratio = (t - start_time) / (end_time - start_time)
            return random_interpolate(start_value, end_value, time_ratio)

    raise ValueError("Invalid input or interpolations")
