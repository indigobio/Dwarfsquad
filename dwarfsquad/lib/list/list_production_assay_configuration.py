from dwarfsquad.model import AssayConfiguration
from dwarfsquad.lib import rest_api
from dwarfsquad.lib.urls import production_assay_configurations


def list_production_assay_configuration(url, data, credentials):

    ac_url = production_assay_configurations(url)
    ac_names = []
    for ac in rest_api.get(ac_url, credentials).json():
        ac = AssayConfiguration(ac)
        ac_names.append(ac.name)

    return '\n'.join(ac_names)