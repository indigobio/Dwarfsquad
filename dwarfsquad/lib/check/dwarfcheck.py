from dwarfsquad.model import AssayConfiguration
from dwarfsquad.lib import collections
from dwarfsquad.lib.check import helpers as check_helpers


def dwarfcheck(url, data, collection, credentials):

    ac = None
    check = None
    if isinstance(data, AssayConfiguration):
        ac = data

    if collection in collections.assay_configuration + collections.production_assay_configurations + collections.full_assay_configuration:
        check = check_helpers.check_assay(ac)

    if collection in collections.lots_and_levels:
        check = check_helpers.check_lots_and_levels(ac)

    if collection in collections.rule_settings:
        check = check_helpers.check_rulesettings(ac)

    if collection in collections.compound_methods:
        check = check_helpers.check_compound_methods(ac)

    return str('\n' + check)
