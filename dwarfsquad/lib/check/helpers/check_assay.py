from check_lots_and_levels import check_lots_and_levels
from check_compound_methods import check_compound_methods
from check_rulesettings import check_rulesettings


def check_assay(ac):
    return check_assay_settings(ac) + check_compound_methods(ac) + check_rulesettings(ac) + check_lots_and_levels(ac)


def check_assay_settings(ac):
    assay_setting_status = []
    assay_setting_status.append("Checking assay settings...")
    assay_setting_status.append("Not Implemented! Skipping.")
    return '\n'.join(assay_setting_status) + '\n\n'