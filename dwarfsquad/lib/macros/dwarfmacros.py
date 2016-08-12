from dwarfsquad.lib.macros.generate_macros import generate_macros
from dwarfsquad.model import AssayConfiguration


def dwarfmacros(url, data, collection, credentials):

    if isinstance(data, AssayConfiguration):
        return str('\n'.join(['\n'] + generate_macros(data) + ['\n']))
