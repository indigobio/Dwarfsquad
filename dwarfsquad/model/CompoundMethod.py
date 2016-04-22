from BaseWebModel import BaseWebModel
from ChromatogramMethod import ChromatogramMethod
from Calibration import Calibration


class CompoundMethod(BaseWebModel):
    required_fields = {
        "name": "",
        "id": "",
        "view_order": 1,
        "chromatogram_methods": [],
        "calibration": Calibration({}),
        "rule_settings": {},
        "enabled_rules_lookup": {}
    }

    @classmethod
    def __str__(cls):
        return "compound method"

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = dict(base.items() + arg.items())

        BaseWebModel.__init__(self, self.build_entities_with_id(base))
        self.set_calibration(Calibration(self.calibration))
        self.chromatogram_methods = self.enumerate_arrays(ChromatogramMethod, self.chromatogram_methods)

    def set_name(self, name):
        assert isinstance(name, basestring)
        self.name = name

    def set_view_order(self, view_order):
        assert isinstance(int(view_order), int)
        self.view_order = int(view_order)

    def set_calibration(self, calibration):
        assert isinstance(calibration, Calibration)
        self.calibration = calibration