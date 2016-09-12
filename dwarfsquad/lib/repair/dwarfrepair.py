from dwarfsquad.model.AssayConfiguration import AssayConfiguration
from dwarfsquad.lib import collections
from dwarfsquad.lib.repair import helpers as repair_helpers


def dwarfrepair(url, data, collection, credentials):

    ac = None
    if isinstance(data, AssayConfiguration):
        ac = data

    if collection in collections.assay_configuration + collections.production_assay_configurations + collections.full_assay_configuration:
        ac = repair_helpers.repair_assay(ac)

    if collection in collections.lots_and_levels:
        ac = repair_helpers.repair_lots_and_levels(ac)

    if collection in collections.rule_settings:
        ac = repair_helpers.repair_rulesettings(ac)

    if collection in collections.compound_methods:
        ac = repair_helpers.repair_compound_methods(ac)

    return ac
