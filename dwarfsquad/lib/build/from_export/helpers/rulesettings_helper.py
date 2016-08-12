from dwarfsquad.lib.utils import to_stderr
import os
from .csv_helper import read_csv


def get_rulesettings_csv(path_to_export):

    export_dir = os.path.abspath(path_to_export)
    rulesettings_csv = os.path.join(export_dir, 'rulesettings.csv')
    try:
        assert os.path.exists(rulesettings_csv)
    except AssertionError:
        to_stderr("Could not find rulesettings.csv. Skipping.")
        return []

    return read_csv(rulesettings_csv)


def get_enabled_rules(rulesettings_list, cm):
    enabled_rules_lookup = {}
    for row in rulesettings_list:
        if row['context'] == 'compound' and row['compound'] == cm.name:
            for column, value in row.items():
                if column and value.lower() == 'enabled':
                    enabled_rules_lookup[column] = True
                elif column and value.lower() == 'disabled':
                    enabled_rules_lookup[column] = False

    return enabled_rules_lookup


def get_settings(rulesettings_list, reference_map, cm, context='compound'):

    settings = {}
    for row in rulesettings_list:
        if row['context'] == context and row['compound'] == cm.name:
            for column, value in row.items():
                if column and value.lower() not in ['enabled', 'disabled', cm.name.lower(), context.lower(), 'ignore']:
                    try:
                        referenced_value = reference_map[str(value)]
                        if referenced_value:
                            settings[column] = referenced_value
                    except KeyError:
                        if value:
                            settings[column] = str(value)
                        else:
                            pass

    return settings
