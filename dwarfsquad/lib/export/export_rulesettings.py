import csv
from collections import OrderedDict
from dwarfsquad.lib.utils import to_stderr
from dwarfsquad.model import AssayConfiguration
from dwarfsquad.lib.build.from_export import helpers as export_helpers


def export_rulesettings(ac):

    assert isinstance(ac, AssayConfiguration)

    rows = get_rulesettings_rows(ac)
    keys = get_rulesettings_keys(rows)

    with open('rulesettings.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=keys, restval='', )
        writer.writeheader()
        writer.writerows(rows)
        to_stderr("Wrote rulesettings and rules enabled to rulesettings.csv")


def get_rulesettings_keys(rows):
    keys = []
    for item in rows:
        keys.extend([key for key in item.keys() if key not in keys])
    return keys


def get_rulesettings_rows(ac):
    reference_map = export_helpers.build_reference_map(ac.compound_methods)
    compound_rows = []
    chromatogram_rows = []
    for cm in ac.compound_methods:
        row = OrderedDict()
        row['compound'] = cm.name
        row['context'] = 'compound'

        for schema in sorted(ac.qa_rule_schemas, key=lambda k: k.name):
            row[schema.name] = get_rule_enabled(cm, schema.name)
            for param in schema.rule_parameters:
                if param.scope == "compound":
                    row[param.name] = get_rulesetting(cm, param.name, reference_map)
        row["CHROMATOGRAM SETTINGS"] = 'IGNORE'
        compound_rows.append(row)

        for ch_m in cm.chromatogram_methods:
            row = OrderedDict()
            row['compound'] = cm.name
            row['context'] = ch_m.name
            for schema in ac.qa_rule_schemas:
                for param in schema.rule_parameters:
                    if param.scope == "chromatogram":
                        row[param.name] = get_rulesetting(ch_m, param.name, reference_map)
            chromatogram_rows.append(row)
    compound_rows.extend(chromatogram_rows)
    return compound_rows


def resolve_or_return(param, reference_map):
    try:
        return reference_map[param]
    except KeyError:
        return param


def get_rulesetting(method, param_name, reference_map):
    if param_name in method.rule_settings:
        return resolve_or_return(method.rule_settings[param_name], reference_map)


def get_rule_enabled(cm, rule_name):
    if rule_name in cm.enabled_rules_lookup and cm.enabled_rules_lookup[rule_name]:
        return "Enabled"
    else:
        return "Disabled"