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
from numpy.random import choice


def pick_transition(et, smap):
    """
    Pick a transition in a set of transitions based on the weights
    specified by the stochastic map

    Parameters
    --------------
    et
        Enabled transitions
    smap
        Stochastic map

    Returns
    --------------
    trans
        Transition chosen according to the weights
    """
    wmap = {ct: smap[ct].get_weight() if ct in smap else 1.0 for ct in et}
    wmap_sv = sum(wmap.values())
    list_of_candidates = []
    probability_distribution = []
    for ct in wmap:
        list_of_candidates.append(ct)
        if wmap_sv == 0:
            probability_distribution.append(1.0/float(len(wmap)))
        else:
            probability_distribution.append(wmap[ct] / wmap_sv)
    ct = list(choice(et, 1, p=probability_distribution))[0]
    return ct
