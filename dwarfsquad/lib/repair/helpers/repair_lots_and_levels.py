from copy import deepcopy
from dwarfsquad.lib.utils import to_stderr
from dwarfsquad.model.AssayConfiguration import AssayConfiguration
from dwarfsquad.model.Level import ControlMaterial
from dwarfsquad.model.Lot import LotCompound as LotCompound


def repair_lots_and_levels(ac):
    try:
        assert isinstance(ac, AssayConfiguration)
    except:
        raise AssertionError("ac is type: " + str(type(ac)))

    compound_method_names = [cm.name for cm in ac.compound_methods]

    to_stderr("Repairing lots/levels by removing compounds no longer found in assay configuration.")

    new_lots = []
    for lot_data in ac.lots:
        lot = deepcopy(lot_data)
        new_lot_compounds = []
        to_stderr("\tRemoving the following compounds from " + lot.name + ":")
        for comp in lot.compounds:
            if comp.name not in compound_method_names:
                to_stderr("\t\t" + comp.name)
            else:
                new_lot_compounds.append(comp)
        to_stderr("\tAdding the following compounds to " + lot.name + ":")
        for cm in ac.compound_methods:
            if cm.calibration.enabled and cm.name not in [comp.name for comp in lot.compounds]:
                to_stderr("\t\t" + cm.name)
                new_lot_compounds.append(LotCompound({'name': cm.name, 'included': True}))

        lot.compounds = new_lot_compounds

        new_levels = []
        for level in lot.levels:
            to_stderr("\tRemoving the following compounds " + lot.name + "/" + level.name + ":")
            new_control_material = []
            for control_material in level.control_material:
                if control_material.name not in compound_method_names:
                    to_stderr("\t\t" + control_material.name)
                else:
                    new_control_material.append(control_material)

            to_stderr("\tAdding the following compounds to " + lot.name + "/" + level.name + ":")
            for cm in ac.compound_methods:
                if cm.calibration.enabled and cm.name not in [ctrl_mat.name for ctrl_mat in level.control_material]:
                    to_stderr("\t\t" + cm.name)
                    new_control_material.append(ControlMaterial({
                        'name': cm.name,
                        'nominal_conc': 0.0,
                        'std_dev': 0.0}))

            level.control_material = new_control_material
            new_levels.append(level)

        lot.levels = new_levels
        new_lots.append(lot)

    ac.lots = new_lots

    return ac
