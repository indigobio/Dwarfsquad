import csv
from openpyxl import load_workbook
import io
from dwarfsquad.lib.build.from_export import build_compound_methods, build_lots_and_levels
from dwarfsquad.lib.build.from_export.build_assay_configuration import build_assay_configuration
from dwarfsquad.lib.build.from_export.build_rulesettings import add_rules_to_methods
from dwarfsquad.lib.macros.generate_macros import generate_macros

__author__ = 'ktussey'


def build_full_ac(path_to_xlsx):
    wb = load_workbook(path_to_xlsx)
    ac = build_assay_configuration(read_csv_from_sheet(wb.get_sheet_by_name('Assay')))
    ac.compound_methods = build_compound_methods(read_csv_from_sheet(wb.get_sheet_by_name('Compound')))
    ac.lots = build_lots_and_levels(read_csv_from_sheet(wb.get_sheet_by_name('Lots')))
    ac.compound_methods = add_rules_to_methods(read_csv_from_sheet(wb.get_sheet_by_name('Rule')), ac.compound_methods)
    if not ac.macros:
        ac.macros = generate_macros(ac)
    return ac


def get_column_value(c):
    if c.value:
        return unicode(c.value)
    else:
        return unicode('')


def read_csv_from_sheet(worksheet):
    stream = io.StringIO()
    for row in worksheet.rows:
        stream.write(','.join([get_column_value(c) for c in row]))
        stream.write(unicode('\n'))
    reader = csv.DictReader(stream.getvalue().splitlines())
    rows = [r for r in reader]
    return rows