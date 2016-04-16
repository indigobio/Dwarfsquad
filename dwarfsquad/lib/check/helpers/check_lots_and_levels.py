from dwarfsquad.lib.utils import assert_assay_configuration


def find_orphan_compounds_in_level(orphan_compounds, compound_method_names, lot):
    lots_levels_status = []
    for level in lot.levels:
        lots_levels_status.append("\tCompounds without methods in Lot/Level: " + lot.name + "/" + level.name)
        for cm in level.control_material:
            if cm.name not in compound_method_names + orphan_compounds:
                lots_levels_status.append("\t\t" + cm.name)
    return lots_levels_status


def find_orphan_compounds_in_lot(compound_method_names, lot):
    orphan_compounds = []
    for comp in lot.compounds:
        if comp.name not in compound_method_names:
            orphan_compounds.append(comp.name)
    return orphan_compounds


def get_lots_levels_report(ac, compound_method_names):
    lots_levels_status = []
    for lot in ac.lots:
        lots_levels_status.append("\tCompounds without methods in Lot: " + lot.name)
        orphan_compounds = find_orphan_compounds_in_lot(compound_method_names, lot)
        for orphan_compound in orphan_compounds:
            lots_levels_status.append("\t\t" + orphan_compound)
        lots_levels_status.extend(find_orphan_compounds_in_level(orphan_compounds, compound_method_names, lot))
    return lots_levels_status


def get_all_lots_levels_compounds(ac):
    all_compound_names = set()
    for lot in ac.lots:
        for comp in lot.compounds:
            all_compound_names.add(comp.name)
    return all_compound_names


def find_lots_without_compound(ac, compound_name):
    lots_without_compound = []
    for lot in ac.lots:
        if compound_name not in [comp.name for comp in lot.compounds]:
            lots_without_compound.append(lot.name)
    return lots_without_compound


def get_missing_compounds_report(ac):
    lots_levels_status = ["\n\n\tCompounds not found in any Lots:"]
    all_lots_levels_compounds = get_all_lots_levels_compounds(ac)
    for cm in ac.compound_methods:
        if cm.name not in all_lots_levels_compounds and cm.calibration.enabled:
            lots_levels_status.append("\t\t" + cm.name)

    lots_levels_status.append("\n\n\tCompounds found in at least one Lot, but were missing from the following Lots:")
    for cm in ac.compound_methods:
        lots_without_compound = find_lots_without_compound(ac, cm.name)
        if lots_without_compound and cm.calibration.enabled:
            lots_levels_status.append("\t\t" + cm.name + ":")
            lots_levels_status.extend(["\t\t\t" + lot_name for lot_name in lots_without_compound])
    return lots_levels_status


def check_lots_and_levels(ac):
    assert_assay_configuration(ac)
    compound_method_names = [cm.name for cm in ac.compound_methods]
    lots_levels_status = get_lots_levels_report(ac, compound_method_names)
    lots_levels_status.extend(get_missing_compounds_report(ac))

    return '\n'.join(lots_levels_status) + '\n\n'
