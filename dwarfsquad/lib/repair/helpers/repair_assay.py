from dwarfsquad.lib.utils import to_stderr
from dwarfsquad.lib.repair.helpers.repair_lots_and_levels import repair_lots_and_levels
from dwarfsquad.lib.repair.helpers.repair_compound_methods import repair_compound_methods
from dwarfsquad.lib.repair.helpers.repair_rulesettings import repair_rulesettings


def repair_assay(ac):
    return repair_assay_settings(repair_lots_and_levels(repair_rulesettings(repair_compound_methods(ac))))


def repair_assay_settings(ac):
    to_stderr("Repairing assay settings...")
    to_stderr("Not Implemented! Skipping.")
    return ac
