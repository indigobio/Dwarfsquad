from dwarfsquad.lib import collections
from dwarfsquad.lib.download.download_batch import download_batch


def dwarfdownload(url, data, collection, credentials, update=False):
    if isinstance(data, str) and collection in collections.batch:
        return download_batch(url, data, credentials)
