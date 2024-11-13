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
from collections import Counter
from enum import Enum

from pm4py.util import constants, exec_utils
from pm4py.util import xes_constants as xes_util
from typing import Optional, Dict, Any, Union, Tuple
from pm4py.objects.log.obj import EventLog, EventStream


class Parameters(Enum):
    ACTIVITY_KEY = constants.PARAMETER_CONSTANT_ACTIVITY_KEY


def apply(log: Union[EventLog, EventStream], parameters: Optional[Dict[Union[str, Parameters], Any]] = None) -> Dict[Tuple[str, str, str], int]:
    return freq_triples(log, parameters=parameters)


def freq_triples(log: Union[EventLog, EventStream], parameters: Optional[Dict[Union[str, Parameters], Any]] = None) -> Dict[Tuple[str, str, str], int]:
    """
    Counts the number of directly follows occurrences, i.e. of the form <...a,b...>, in an event log.

    Parameters
    ----------
    log
        Trace log
    parameters
        Possible parameters passed to the algorithms:
            activity_key -> Attribute to use as activity

    Returns
    -------
    dfg
        DFG graph
    """
    if parameters is None:
        parameters = {}
    activity_key = exec_utils.get_param_value(Parameters.ACTIVITY_KEY, parameters, xes_util.DEFAULT_NAME_KEY)
    dfgs = map(
        (lambda t: [(t[i - 2][activity_key], t[i - 1][activity_key], t[i][activity_key]) for i in range(2, len(t))]),
        log)
    return dict(Counter([dfg for lista in dfgs for dfg in lista]))
