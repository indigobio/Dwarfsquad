try:
    from urllib.parse import urljoin, urlparse
except ImportError:
    from urlparse import urljoin, urlparse


def assay_configurations(url):
    return urljoin(url, 'assay_configurations/')


def assay_configuration(url, assay_id):
    url = assay_configurations(url)
    url = urljoin(url, str(assay_id) + '/')
    return url


def production_assay_configurations(url):
    return urljoin(url, 'production_assay_configurations/')


def batches_upload(url):
    parsed = urlparse(url)
    client = parsed.hostname.split('.')[0]
    domain = parsed.hostname.split('.')[1:]
    port = parsed.port
    url = parsed.scheme + "://quartermaster." + '.'.join(domain)
    if port:
        url += ":" + str(port)


    url = urljoin(url, 'batches/upload/' + client)
    return url


def batch(url):
    return urljoin(url, "batch/")


def batches(url, batch_id):
    url = urljoin(url, "batches/")
    return urljoin(url, str(batch_id))


def batches_json(url):
    url = urljoin(url, "batches.json")
    return url


def batch_download(url, batch_id):
    url = urljoin(batch(url), "download/")
    url = urljoin(url, str(batch_id) + "?partial=true")
    return url
