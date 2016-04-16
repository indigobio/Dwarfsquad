from BaseWebModel import BaseWebModel


class Smoothing(BaseWebModel):
    required_fields = {
        "optimal_enabled": True,
        "fixed": "",
        "min": "4",
        "max": "22",
        "start": "8"
    }

    @classmethod
    def __str__(cls):
        return "smoothing"

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            if isinstance(arg, dict):
                base = dict(base.items() + arg.items())

        BaseWebModel.__init__(self, self.build_required_entities_only(base))

    def set_max(self, max):
        assert isinstance(float(max), float)
        self.max = max

    def set_optimal_enabled(self, optimal_enabled):
        self.optimal_enabled = str(optimal_enabled).lower() == 'true'

    def set_min(self, min):
        assert isinstance(float(min), float)
        self.min = min

    def set_start(self, start):
        assert isinstance(float(start), float)
        self.start = start

    def set_fixed(self, fixed):     
        try:
            self.fixed = int(fixed)
        except ValueError:
            self.fixed = None