from BaseWebModel import BaseWebModel
from ReductionMethod import ReductionMethod
from PeakIntegration import PeakIntegration


class ChromatogramMethod(BaseWebModel):
    required_fields = {
        "name": "",
        "reduction_method": ReductionMethod({}),
        "peak_integration": PeakIntegration({}),
        "rule_settings": {}
    }

    @classmethod
    def __str__(cls):
        return "chromatogram method"

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = dict(base.items() + arg.items())

        BaseWebModel.__init__(self, self.build_entities_with_id(base))
        self.set_reduction_method(ReductionMethod(self.reduction_method))
        self.set_peak_integration(PeakIntegration(self.peak_integration))

    def set_name(self, name):
        assert isinstance(name, basestring)
        self.name = name

    def set_reduction_method(self, reduction_method):
        assert isinstance(reduction_method, ReductionMethod)
        self.reduction_method = reduction_method

    def set_peak_integration(self, peak_integration):
        assert isinstance(peak_integration, PeakIntegration)
        self.peak_integration = peak_integration

    def set_type(self, ch_type):
        assert isinstance(ch_type, basestring)
        self.type = ch_type