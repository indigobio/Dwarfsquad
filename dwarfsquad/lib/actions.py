from build import dwarfbuild
from upload import dwarfupload
from macros import dwarfmacros
from repair import dwarfrepair
from list import dwarflist
from export import dwarfexport
from check import dwarfcheck


def build(url, credentials, data, collection):
    from dwarfsquad.lib.utils import to_stderr
    to_stderr("Building " + str(data))
    return dwarfbuild(data)


def export(url, credentials, data, collection):
    from dwarfsquad.lib.utils import to_stderr
    to_stderr("Exporting " + str(data))
    return dwarfexport(url, dwarfbuild(data), collection, credentials)


def check(url, credentials, data, collection):
    from dwarfsquad.lib.utils import to_stderr
    to_stderr("Checking " + str(data))
    return dwarfcheck(url, dwarfbuild(data), collection, credentials)


def repair(url, credentials, data, collection):
    from dwarfsquad.lib.utils import to_stderr
    to_stderr("Checking " + str(data))
    return dwarfrepair(url, dwarfbuild(data), collection, credentials)


def list(url, credentials, data, collection):
    from dwarfsquad.lib.utils import to_stderr
    to_stderr("Listing " + str(collection))
    return dwarflist(url, data, collection, credentials)


def macros(url, credentials, data, collection):
    from dwarfsquad.lib.utils import to_stderr
    to_stderr("Generating macros for " + str(collection))
    return dwarfmacros(url, dwarfbuild(data), collection, credentials)


def upload(url, credentials, data, collection):
    from dwarfsquad.lib.utils import to_stderr
    to_stderr("Uploading " + str(collection) + " data.")
    return dwarfupload(url, dwarfbuild(data), collection, credentials)