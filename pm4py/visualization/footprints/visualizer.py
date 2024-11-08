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
from pm4py.visualization.footprints.variants import comparison, single, comparison_symmetric
from enum import Enum
from pm4py.util import exec_utils, constants
from pm4py.visualization.common import gview
from pm4py.visualization.common import save as gsave
from pm4py.visualization.common.gview import serialize, serialize_dot
import graphviz
from typing import Optional, Dict, Any


class Variants(Enum):
    COMPARISON = comparison
    SINGLE = single
    COMPARISON_SYMMETRIC = comparison_symmetric


def apply(*args, variant=None, parameters: Optional[Dict[Any, Any]] = None) -> graphviz.Source:
    """
    Visualize a footprints table or a comparison between footprints
    tables

    Parameters
    ---------------
    args
        Arguments:
        - A single footprint table
        - Two footprints table (first one associated to the log, second
        one associated to the model)
    parameters
        Parameters of the algorithm, including:
            - Parameters.FORMAT => Format of the visualization

    Returns
    ---------------
    gviz
        Graphviz object
    """
    if parameters is None:
        parameters = {}

    if variant is None:
        if len(args) == 1:
            variant = Variants.SINGLE
        else:
            variant = Variants.COMPARISON

    if variant in [Variants.SINGLE]:
        return exec_utils.get_variant(variant).apply(args[0], parameters=parameters)
    elif variant in [Variants.COMPARISON, Variants.COMPARISON_SYMMETRIC]:
        return exec_utils.get_variant(variant).apply(args[0], args[1], parameters=parameters)


def save(gviz, output_file_path, parameters=None):
    """
    Save the diagram

    Parameters
    -----------
    gviz
        GraphViz diagram
    output_file_path
        Path where the GraphViz output should be saved
    """
    gsave.save(gviz, output_file_path, parameters=parameters)
    return ""


def view(gviz, parameters=None):
    """
    View the diagram

    Parameters
    -----------
    gviz
        GraphViz diagram
    """
    if constants.DEFAULT_ENABLE_VISUALIZATIONS_VIEW:
        return gview.view(gviz, parameters=parameters)


def matplotlib_view(gviz, parameters=None):
    """
    Views the diagram using Matplotlib

    Parameters
    ---------------
    gviz
        Graphviz
    """
    if constants.DEFAULT_ENABLE_VISUALIZATIONS_VIEW:
        return gview.matplotlib_view(gviz, parameters=parameters)
