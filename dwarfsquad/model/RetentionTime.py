import bson
from dwarfsquad.model.BaseWebModel import BaseWebModel
from bson.errors import InvalidId


class RetentionTime(BaseWebModel):
    required_fields = {
        "expected": "",
        "window_width": "0.25",
        "lower_tolerance": "0.25",
        "upper_tolerance": "0.25",
        "reference_type_source": "expected",
        "reference": "",
        "bias": "",
        "upper_trace_width": "",
        "lower_trace_width": "",
        "window_multiplier": "",
        "estimation_width": ""
    }

    @classmethod
    def __str__(cls):
        return "reduction method"

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = {**base, **arg}
        BaseWebModel.__init__(self, self.build_required_entities_only(base))

    def set_expected(self, expected):
        try:
            self.expected = str(float(expected))
        except ValueError:
            self.expected = str(0.0)

    def set_window_width(self, window_width):
        try:
            self.window_width = str(float(window_width))
        except ValueError:
            self.window_width = str(0.25)

    def set_estimation_width(self, estimation_width):
        try:
            self.estimation_width = str(float(estimation_width))
        except ValueError:
            self.estimation_width = str(0.25)

    def set_upper_trace_width(self, upper_trace_width):
        try:
            assert float(upper_trace_width) > 0.0
            self.upper_trace_width = str(float(upper_trace_width))
        except (ValueError, TypeError, AssertionError):
            self.upper_trace_width = None

    def set_lower_trace_width(self, lower_trace_width):
        try:
            assert float(lower_trace_width) > 0.0
            self.lower_trace_width = str(float(lower_trace_width))
        except (ValueError, TypeError, AssertionError):
            self.lower_trace_width = None

    def set_lower_tolerance(self, lower_tolerance):
        try:
            self.lower_tolerance = str(float(lower_tolerance))
        except ValueError:
            self.lower_tolerance = str(0)

    def set_upper_tolerance(self, upper_tolerance):
        try:
            self.upper_tolerance = str(float(upper_tolerance))
        except ValueError:
            self.upper_tolerance = str(0)

    def set_reference_type_source(self, reference_type_source):
        try:
            assert reference_type_source.lower() in ['expected', 'chromatogram', 'samples']
            self.reference_type_source = reference_type_source.lower()
        except AssertionError as e:
            print(reference_type_source)
            raise e

    def set_reference(self, reference):
        try:
            assert reference in ['standard', 'standard_and_qc', 'qc']
            self.reference = reference
        except AssertionError:
            pass

        try:
            bson.ObjectId(reference)
            self.reference = reference
        except InvalidId:
            pass

        self.reference = reference

    def set_bias(self, bias):
        try:
            self.bias = str(float(bias))
        except ValueError:
            self.bias = str(0)

    def set_window_multiplier(self, window_multiplier):
        try:
            self.window_multiplier = str(float(window_multiplier))
        except (ValueError, TypeError):
            self.window_multiplier = None

    def pop_references(self):
        if isinstance(self.reference, dict):
            reference = dict(self.reference)
            self.reference = ''
            return reference
        else:
            return ''
