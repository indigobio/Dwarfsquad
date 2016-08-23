from dwarfsquad.model.BaseWebModel import BaseWebModel


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
                base = {**base, **arg}

        BaseWebModel.__init__(self, self.build_required_entities_only(base))

    def set_max(self, max):
        try:
            int(max)
            self.max = str(int(max))
        except ValueError:
            self.max = str(33)

    def set_optimal_enabled(self, optimal_enabled):
        self.optimal_enabled = str(optimal_enabled).lower() == 'true'

    def set_min(self, min):
        try:
            self.min = str(int(min))
        except ValueError:
            self.min = str(3)

    def set_start(self, start):
        try:
            self.start = str(int(start))
        except ValueError:
            self.start = str(12)

    def set_fixed(self, fixed):     
        try:
            self.fixed = str(int(fixed))
        except ValueError:
            self.fixed = str(12)
