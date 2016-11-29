from dwarfsquad.lib.compat import join_dicts
from dwarfsquad.model.BaseWebModel import BaseWebModel


class Threshold(BaseWebModel):
    required_fields = {
        "absolute_area": "1",
        "relative_area": "0.01",
        "absolute_height": "100",
        "relative_height": "0.01",
        "signal_to_noise": "3",
        "min_merge_difference": "3",
        "first_derivative": "0.25",
        "second_derivative": "0.25",
        "peak_probability": "0.8",
        "relative_low_std_area": "",
        "relative_low_std_height": "",
        "saturation": "100000000"
    }

    @classmethod
    def __str__(cls):
        return "threshold"

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = join_dicts(arg, base)

        BaseWebModel.__init__(self, self.build_required_entities_only(base))

    def set_relative_area(self, relative_area):
        try:
            self.relative_area = str(float(relative_area))
        except ValueError:
            self.relative_area = self.set_to_zero()

    def set_saturation(self, saturation):
        try:
            self.saturation = str(float(saturation))
        except ValueError:
            self.saturation = self.set_to_zero()

    def set_peak_probability(self, peak_probability):
            try:
                self.peak_probability = str(float(peak_probability))
            except ValueError:
                self.peak_probability = self.set_to_zero()

    def set_absolute_area(self, absolute_area):
        try:
            self.absolute_area = str(float(absolute_area))
        except ValueError:
            self.absolute_area = self.set_to_zero()

    def set_min_merge_difference(self, min_merge_difference):
        try:
            self.min_merge_difference = str(float(min_merge_difference))
        except ValueError:
            self.min_merge_difference = self.set_to_zero()

    def set_absolute_height(self, absolute_height):
        try:
            self.absolute_height = str(float(absolute_height))
        except Exception as e:
            self.absolute_height = self.set_to_zero()

    def set_relative_height(self, relative_height):
        try:
            self.relative_height = str(float(relative_height))
        except ValueError:
            self.relative_height = self.set_to_zero()

    def set_signal_to_noise(self, signal_to_noise):
        try:
            self.signal_to_noise = str(float(signal_to_noise))
        except ValueError:
            self.signal_to_noise = self.set_to_zero()

    def set_second_derivative(self, second_derivative):
        try:
            self.second_derivative = str(float(second_derivative))
        except ValueError:
            self.second_derivative = self.set_to_zero()

    def set_first_derivative(self, first_derivative):
        try:
            self.first_derivative = str(float(first_derivative))
        except ValueError:
            self.first_derivative = str(0)

    def set_relative_low_std_area(self, relative_low_std_area):
        try:
            self.relative_low_std_area = str(float(relative_low_std_area))
        except ValueError:
            self.relative_low_std_area = ""

    def set_relative_low_std_height(self, relative_low_std_height):
        try:
            self.relative_low_std_height = str(float(relative_low_std_height))
        except ValueError:
            self.relative_low_std_height = ""

    def set_to_zero(self):
        return str(0)
