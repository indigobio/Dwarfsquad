from dwarfsquad.lib import utils
from dwarfsquad.lib.rest_api import get
from dwarfsquad.lib import urls


def download_batch(url, data, credentials):

    assert isinstance(data, str)
    batch_id = None
    batch_name = None
    batches = get(urls.batches_json(url) + "?search=" + data, credentials).json()

    if utils.is_valid_oid(data):
        batch_id = data
        batch_data = get(urls.batches(url, batch_id), credentials).json()
        if batch_data:
            batch_name = batch_data['name']
        else:
            utils.to_stderr("Could not find any batches with the id: " + data)
    else:
        batch_name = str(data)
        if len(batches) == 1:
            batch_id = batches[0]['_id']
        elif len(batches) > 1:
            utils.to_stderr("Multiple batches satisfy the search requirement.")
        else:
            utils.to_stderr("Could not find any batches with that search.")

    if batch_id and batch_name:
        try:
            r = get(urls.batch_download(url, batch_id), credentials)
            batch_tarball = batch_name + ".tar.gz"
            with open(batch_tarball, "wb") as f:
                utils.to_stderr("Writing: " + batch_tarball)
                for chunk in r.iter_content():
                    f.write(chunk)
            return "Wrote: " + batch_tarball
        except Exception as e:
            utils.to_stderr("An error occurred downloading the batch.")
            return str(e)

    else:
        return "Could not find batch id or batch name. Aborting."
