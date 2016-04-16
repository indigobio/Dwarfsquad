from collections import OrderedDict
import csv
from dwarfsquad.lib.utils import to_stderr
from dwarfsquad.model.Level import ControlMaterial
from dwarfsquad.model import AssayConfiguration


def export_lots_and_levels(ac):

    assert isinstance(ac, AssayConfiguration)
    rows = build_lot_rows(ac)
    try:
        fieldnames = rows[0].keys()
    except IndexError:
        fieldnames = ['type', 'lot', 'level', 'compound', 'nominal_conc', 'std_dev']

    with open('lots_levels.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    to_stderr("Wrote lots and levels to lots_levels.csv!")


def build_lot_rows(ac):
    rows = []
    for lot in ac.lots:
        rows.extend(build_lot_row(lot))
    return rows


def build_lot_row(lot):
    """ @type lot: Lot.Lot """
    type = lot.sample_type
    lot_name = lot.name
    rows = []
    for compound in lot.compounds:
        for level in lot.levels:
            if compound.included:
                new_row = OrderedDict()
                new_row['type'] = type
                new_row['lot'] = lot_name
                new_row['level'] = level.name
                new_row['compound'] = compound.name
                new_row['nominal_conc'] = find_control_material(level, compound.name).nominal_conc
                new_row['std_dev'] = find_control_material(level, compound.name).std_dev
                rows.append(new_row)
    return rows


def find_control_material(level, compound_name):
    for control_material in level.control_material:
        if control_material.name == compound_name:
            return control_material
    return ControlMaterial({'name': compound_name})