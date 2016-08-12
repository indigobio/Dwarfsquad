from dwarfsquad.model.BaseWebModel import BaseWebModel
from dwarfsquad.model.ControlMaterial import ControlMaterial


class Level(BaseWebModel):
    required_fields = {
        'id': '',
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
            base = {**base, **arg}
        BaseWebModel.__init__(self, self.build_entities_with_id(base))
        self.control_material = self.enumerate_arrays(ControlMaterial, self.control_material)

    def set_name(self, name):
        assert isinstance(name, str)
        self.name = name

    def set_control_material(self, control_material):
        assert isinstance(control_material, list)
        self.control_material = control_material
