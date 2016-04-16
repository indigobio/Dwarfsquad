from dwarfsquad.lib import collections
from dwarfsquad.lib.list.list_assay_configuration import list_assay_configuration
from dwarfsquad.lib.list.list_production_assay_configuration import list_production_assay_configuration


def dwarflist(url, data, collection, credentials):

    if collection in collections.production_assay_configurations:
        return list_production_assay_configuration(url, data, credentials)

    if collection in collections.assay_configuration + collections.full_assay_configuration:
        return list_assay_configuration(url, data, credentials)

    raise ValueError(str(collection) + " not a defined collection for list.")