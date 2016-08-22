from dwarfsquad.lib.utils import to_stderr
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
        "saturation": "100000000"
    }

    @classmethod
    def __str__(cls):
        return "threshold"

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = {**base, **arg}

        BaseWebModel.__init__(self, self.build_required_entities_only(base))

    def set_relative_area(self, relative_area):
        assert isinstance(float(relative_area), float)
        self.relative_area = relative_area

    def set_saturation(self, saturation):
        assert isinstance(float(saturation), float)
        self.saturation = saturation

    def set_peak_probability(self, peak_probability):
        assert isinstance(float(peak_probability), float)
        self.peak_probability = peak_probability

    def set_absolute_area(self, absolute_area):
        try:
            assert isinstance(float(absolute_area), float)
            self.absolute_area = absolute_area
        except Exception as e:
            to_stderr(str(e))
            to_stderr("Setting absolute_area to 0")
            self.absolute_area = 0

    def set_min_merge_difference(self, min_merge_difference):
        assert isinstance(float(min_merge_difference), float)
        self.min_merge_difference = min_merge_difference

    def set_absolute_height(self, absolute_height):
        try:
            assert isinstance(float(absolute_height), float)
            self.absolute_height = absolute_height
        except Exception as e:
            to_stderr(str(e))

    def set_relative_height(self, relative_height):
        assert isinstance(float(relative_height), float)
        self.relative_height = relative_height

    def set_signal_to_noise(self, signal_to_noise):
        assert isinstance(float(signal_to_noise), float)
        self.signal_to_noise = signal_to_noise

    def set_second_derivative(self, second_derivative):
        assert isinstance(float(second_derivative), float)
        self.second_derivative = second_derivative

    def set_first_derivative(self, first_derivative):
        assert isinstance(float(first_derivative), float)
        self.first_derivative = first_derivative
