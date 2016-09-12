from dwarfsquad.lib.compat import join_dicts
from dwarfsquad.model.BaseWebModel import BaseWebModel


class LotCompound(BaseWebModel):
    required_fields = {
        'name': '',
        'included': False
    }

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = join_dicts(arg, base)

        BaseWebModel.__init__(self, self.build_required_entities_only(base))

    def set_name(self, name):
        assert isinstance(name, str)
        self.name = name

    def set_included(self, included):
        self.included = str(included).lower() == 'true'
