import urlparse


def assay_configurations(url):
    return urlparse.urljoin(url, 'assay_configurations/')


def assay_configuration(url, assay_id):
    url = assay_configurations(url)
    url = urlparse.urljoin(url, str(assay_id) + '/')
    return url


def production_assay_configurations(url):
    return urlparse.urljoin(url, 'production_assay_configurations/')


def batches_upload(url):
    parsed = urlparse.urlparse(url)
    client = parsed.hostname.split('.')[0]
    domain = parsed.hostname.split('.')[1:]
    port = parsed.port
    url = parsed.scheme + "://quartermaster." + '.'.join(domain)
    if port:
        url += ":" + port

    url = urlparse.urljoin(url, 'batches/upload/' + client)
    return url