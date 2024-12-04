import os
import pm4py
from pm4py.objects.petri_net.obj import PetriNet, Marking
from pm4py.objects.bpmn.importer import importer as bpmn_importer
from pm4py.objects.conversion.bpmn import converter as bpmn_converter
from pm4py.objects.petri_net.utils import petri_utils
import examples_conf
import importlib.util


def execute_script():
    #running-example
    file_name = "d16"
    bpmn_graph = bpmn_importer.apply(os.path.join("..", "tests", "input_data", file_name + ".bpmn"))
    net, im, fm = bpmn_converter.apply(bpmn_graph, variant=bpmn_converter.Variants.TO_PETRI_NET)

    if False:
        if importlib.util.find_spec("graphviz"):
            pm4py.view_petri_net(net, im, fm, format=examples_conf.TARGET_IMG_FORMAT)

        pm4py.write_pnml(net, im, fm, os.path.join("..", "tests", "input_data", file_name + ".pnml"))


if __name__ == "__main__":
    execute_script()
