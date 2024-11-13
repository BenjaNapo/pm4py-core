'''
    PM4Py – A Process Mining Library for Python
Copyright (C) 2024 Process Intelligence Solutions UG (haftungsbeschränkt)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see this software project's root or
visit <https://www.gnu.org/licenses/>.

Website: https://processintelligence.solutions
Contact: info@processintelligence.solutions
'''
from enum import Enum


def unroll(value):
    if isinstance(value, Enum):
        return value.value
    return value


# this function can be moved to a util when string values of the parameters are no longer supported. (or is no longer needed ;-))
def get_param_value(p, parameters, default):
    if parameters is None:
        return unroll(default)
    unrolled_parameters = {}
    for p0 in parameters:
        unrolled_parameters[unroll(p0)] = parameters[p0]
    if p in parameters:
        val = parameters[p]
        return unroll(val)
    up = unroll(p)
    if up in unrolled_parameters:
        val = unrolled_parameters[up]
        return unroll(val)
    return unroll(default)


def get_variant(variant):
    if isinstance(variant, Enum):
        return variant.value
    return variant
