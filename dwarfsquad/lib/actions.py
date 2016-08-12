from dwarfsquad.lib.build.dwarfbuild import dwarfbuild
from dwarfsquad.lib.upload import dwarfupload
from dwarfsquad.lib.macros import dwarfmacros
from dwarfsquad.lib.repair import dwarfrepair
from dwarfsquad.lib.list import dwarflist
from dwarfsquad.lib.export import dwarfexport
from dwarfsquad.lib.check import dwarfcheck


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
