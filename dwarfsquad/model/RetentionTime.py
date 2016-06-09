import bson
from BaseWebModel import BaseWebModel
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
        "estimation_width": ""
    }

    @classmethod
    def __str__(cls):
        return "reduction method"

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = dict(base.items() + arg.items())
        BaseWebModel.__init__(self, self.build_required_entities_only(base))

    def set_expected(self, expected):
        try:
            self.expected = float(expected)
        except ValueError:
            self.expected = 0.0

    def set_window_width(self, window_width):
        try:
            self.window_width = float(window_width)
        except ValueError:
            self.window_width = 0.25

    def set_estimation_width(self, estimation_width):
        try:
            self.estimation_width = float(estimation_width)
        except ValueError:
            self.estimation_width = 0.25

    def set_upper_trace_width(self, upper_trace_width):
        try:
            assert float(upper_trace_width) > 0.0
            self.upper_trace_width = float(upper_trace_width)
        except (ValueError, TypeError, AssertionError):
            self.upper_trace_width = ""

    def set_lower_trace_width(self, lower_trace_width):
        try:
            assert float(lower_trace_width) > 0.0
            self.lower_trace_width = float(lower_trace_width)
        except (ValueError, TypeError, AssertionError):
            self.lower_trace_width = ""

    def set_lower_tolerance(self, lower_tolerance):
        try:
            self.lower_tolerance = float(lower_tolerance)
        except ValueError:
            self.lower_tolerance = 0.25

    def set_upper_tolerance(self, upper_tolerance):
        try:
            self.upper_tolerance = float(upper_tolerance)
        except ValueError:
            self.upper_tolerance = 0.25

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
            self.bias = float(bias)
        except ValueError:
            self.bias = 0.0

    def pop_references(self):
        if isinstance(self.reference, dict):
            reference = dict(self.reference)
            self.reference = ''
            return reference
        else:
            return ''