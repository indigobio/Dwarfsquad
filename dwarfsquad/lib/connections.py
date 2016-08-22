from requests.exceptions import SSLError
import requests
from dwarfsquad.lib import urls as urls
from dwarfsquad.lib.exceptions import AuthorizationError
from dwarfsquad.lib.utils import to_stderr


def site_exists(url):

    try:
        requests.get(url)
        return True
    except SSLError as e:
        to_stderr(e)
        return True
    except requests.ConnectionError:
        return False


def can_login(url, credentials):
    try:
        response = requests.get(urls.assay_configurations(url), auth=credentials)
        if 'sign_in' in response.url:
            raise AuthorizationError(url)
        else:
            return response.url == urls.assay_configurations(url) and response.status_code == 200

    except requests.ConnectionError:
        return site_exists(url)

    except Exception as e:
        to_stderr(e)
        return False
