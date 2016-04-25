from BaseWebModel import BaseWebModel


class Level(BaseWebModel):
    required_fields = {
        'name': '',
        'control_material': []
    }

    @classmethod
    def __str__(cls):
        return "level"

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = dict(base.items() + arg.items())
        BaseWebModel.__init__(self, self.build_entities_with_id(base))
        self.control_material = self.enumerate_arrays(ControlMaterial, self.control_material)

    def set_name(self, name):
        assert isinstance(name, basestring)
        self.name = name

    def set_control_material(self, control_material):
        assert isinstance(control_material, list)
        self.control_material = control_material


class ControlMaterial(BaseWebModel):
    required_fields = {
        'name': '',
        'nominal_conc': '',
        'std_dev': 0.0
    }

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = dict(base.items() + arg.items())

        BaseWebModel.__init__(self, self.build_required_entities_only(base))

    def set_name(self, name):
        assert isinstance(name, basestring)
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