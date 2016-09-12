from dwarfsquad.lib.compat import join_dicts
from dwarfsquad.model.BaseWebModel import BaseWebModel


class ControlMaterial(BaseWebModel):
    required_fields = {
        'name': '',
        'nominal_conc': 0.0,
        'std_dev': 0.0
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

    def set_nominal_conc(self, nominal_conc):
        try:
            self.nominal_conc = float(nominal_conc)
        except ValueError:
            self.nominal_conc = 0.0

    def set_std_dev(self, std_dev):
        try:
            self.std_dev = float(std_dev)
        except ValueError:
            self.std_dev = 0.0
