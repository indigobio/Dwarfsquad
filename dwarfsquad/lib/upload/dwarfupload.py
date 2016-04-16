from upload_batch import upload_batch
from dwarfsquad.model.Batch import Batch
from dwarfsquad.lib import collections


def dwarfupload(url, data, collection, credentials, update=False):
    if isinstance(data, Batch) and collection in collections.batch:
        return upload_batch(url, data, credentials)