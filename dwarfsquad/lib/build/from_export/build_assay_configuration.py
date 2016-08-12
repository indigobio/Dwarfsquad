import os
from dwarfsquad.lib.build.from_export import helpers
from dwarfsquad.lib.macros.generate_macros import generate_macros
from dwarfsquad.model import AssayConfiguration
from dwarfsquad.model.DisplaySettings import DisplaySettings
from dwarfsquad.lib.build.from_export.build_compound_methods import build_compound_methods
from dwarfsquad.lib.build.from_export.build_lots_and_levels import build_lots_and_levels
from dwarfsquad.lib.build.from_export.build_rulesettings import add_rules_to_methods


def build_full_assay_configuration(path_to_export):
    export_dir = os.path.abspath(path_to_export)
    assert os.path.isdir(export_dir)
    assay_name = helpers.get_assay_name(export_dir)
    ac = build_assay_configuration(helpers.get_assay_csv(path_to_export))
    ac.set_name(assay_name)
    ac.compound_methods = build_compound_methods(helpers.get_compounds_csv(path_to_export))
    ac.lots = build_lots_and_levels(helpers.get_lots_levels_csv(path_to_export))
    ac.compound_methods = add_rules_to_methods(helpers.get_rulesettings_csv(path_to_export), ac.compound_methods)
    if not ac.macros:
        ac.macros = generate_macros(ac)
    return ac


def build_assay_configuration(assay_csv):

    ac = AssayConfiguration({})
    display_settings = DisplaySettings({})

    for row in assay_csv:
        if row['instruments']:
            ac.instruments.extend([row['instruments']])
        if row['macros']:
            ac.macros.extend([row['macros']])
        if row['property_key']:
            ac.properties[row['property_key']] = row['property_value']
        if row['name']:
            ac.set_name(row['name'])
        if row['compute_version']:
            ac.set_compute_version(row['compute_version'])
        if row['peak_area_format']:
            display_settings.set_peak_area_format(row['peak_area_format'])
        if row['concentration_format']:
            display_settings.set_concentration_format(row['concentration_format'])
        if row['response_format']:
            display_settings.set_response_format(row['response_format'])
        if row['review_method']:
            display_settings.set_review_method(row['review_method'])

    ac.set_display_settings(display_settings)
    return ac
