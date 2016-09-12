from dwarfsquad.model.Lot import Lot
from dwarfsquad.model.Level import Level
from dwarfsquad.model.Level import ControlMaterial
from dwarfsquad.model.Lot import LotCompound


def build_lots_and_levels(lotslevels_csv):

    lots = []
    for row in lotslevels_csv:
        lot_index, lot = get_lot(lots, row)
        lot_compound_index, lot_compound = get_lot_compound(lot, row)
        lot.compounds.insert(lot_compound_index, lot_compound)

        level_index, level = get_level(lot, row)
        control_material_index, control_material = get_control_material(level, row)

        if lot_compound.included:
            level.control_material.insert(control_material_index, control_material)
        lot.levels.insert(level_index, level)
        lots.insert(lot_index, lot)

    return lots


def get_control_material(level, row):

    for index, control_material in enumerate(level.control_material):
        if control_material.name == row['compound']:
            return index, level.control_material.pop(index)

    control_material = ControlMaterial({})
    control_material.set_name(row['compound'])
    control_material.set_nominal_conc(row['nominal_conc'])
    control_material.set_std_dev(row['std_dev'])
    return len(level.control_material), control_material


def get_lot_compound(lot, row):

    for index, compound in enumerate(lot.compounds):
        if compound.name == row['compound']:
            return index, lot.compounds.pop(index)

    compound = LotCompound({})
    compound.set_name(row['compound'])
    if 'included' in row:
        compound.set_included(row['included'])
    else:
        compound.set_included(True)
    return len(lot.compounds), compound


def get_lot(lots, row):

    for index, lot in enumerate(lots):
        if lot.name == row['lot']:
            return index, lots.pop(index)

    lot = Lot({})
    lot.name = row['lot']
    lot.sample_type = row['type']
    return len(lots), lot


def get_level(lot, row):

    for index, level in enumerate(lot.levels):
        if level.name == row['level']:
            return index, lot.levels.pop(index)

    level = Level({})
    level.name = row['level']
    return len(lot.levels), level
