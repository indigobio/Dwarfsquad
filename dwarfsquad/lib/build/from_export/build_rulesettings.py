import helpers as export_helpers


def add_rules_to_methods(rulesettings_list, cms):
    reference_map = export_helpers.build_reference_map(cms)
    new_cms = []
    for cm in cms:
        cm.enabled_rules_lookup = export_helpers.get_enabled_rules(rulesettings_list, cm)
        cm.rule_settings = export_helpers.get_settings(rulesettings_list, reference_map, cm)
        for ch_m in cm.chromatogram_methods:
            ch_m.rule_settings = export_helpers.get_settings(rulesettings_list, reference_map, cm, ch_m.name)
        new_cms.append(cm)
    return new_cms