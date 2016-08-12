from collections import OrderedDict
import csv
from dwarfsquad.lib.utils import to_stderr
from dwarfsquad.model import AssayConfiguration


def export_assay_configuration(ac):

    try:
        assert isinstance(ac, AssayConfiguration)
    except:
        raise AssertionError("ac is type " + str(type(ac)))

    rows = get_assay_configuration_rows(ac)

    with open('assay.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
        to_stderr("Wrote assay configuration to assay.csv")


def get_assay_configuration_rows(ac):

    rows = []
    row = OrderedDict()
    row['compute_version'] = ac.compute_version
    row['name'] = ac.name
    row['peak_area_format'] = ac.display_settings.peak_area_format
    row['concentration_format'] = ac.display_settings.concentration_format
    row['response_format'] = ac.display_settings.response_format
    row['review_method'] = ac.display_settings.review_method
    instruments = iter(ac.instruments)
    macros = iter(ac.macros)
    properties = iter(ac.properties.copy().items())

    has_stuff_left = True
    while has_stuff_left:

        has_stuff_left = False
        try:
            row['instruments'] = next(instruments)
            has_stuff_left = True
        except (ValueError, StopIteration):
            row['instruments'] = ''

        try:
            row['macros'] = next(macros)
            has_stuff_left = True
        except (ValueError, StopIteration):
            row['macros'] = ''

        try:
            prop = next(properties)
            row['property_key'] = prop[0]
            row['property_value'] = prop[1]
            has_stuff_left = True
        except (ValueError, StopIteration):
            row['property_key'] = ''
            row['property_value'] = ''

        rows.append(row)
        row = OrderedDict()
        row['compute_version'] = ''
        row['name'] = ''
        row['peak_area_format'] = ''
        row['concentration_format'] = ''
        row['response_format'] = ''
        row['review_method'] = ''

    return rows
