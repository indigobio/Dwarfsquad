import requests
from dwarfsquad.lib import urls
from dwarfsquad.lib.utils import to_stderr
from dwarfsquad.model.Batch import Batch


def upload_batch(url, data, credentials):

    assert isinstance(data, Batch)
    url = urls.batches_upload(url)
    to_stderr("Uploading batch to " + str(url))
    data.open()
    response = requests.post(url, data={'checksum': data.checksum}, files={'file': data.file}, auth=credentials)
    data.close()
    return response.json()