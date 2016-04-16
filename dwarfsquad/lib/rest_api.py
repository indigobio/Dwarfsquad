import requests


def get(url, credentials):
    return requests.get(url, auth=credentials)