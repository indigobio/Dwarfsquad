from dwarfsquad.lib.compat import join_dicts
from dwarfsquad.model.BaseWebModel import BaseWebModel
from dwarfsquad.model.ReductionMethod import ReductionMethod
from dwarfsquad.model.PeakIntegration import PeakIntegration


class ChromatogramMethod(BaseWebModel):
    required_fields = {
        "name": "",
        "id": "",
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
            base = join_dicts(arg, base)

        BaseWebModel.__init__(self, self.build_entities_with_id(base))
        self.set_reduction_method(ReductionMethod(self.reduction_method))
        self.set_peak_integration(PeakIntegration(self.peak_integration))

    def set_name(self, name):
        assert isinstance(name, str)
        self.name = name

    def set_reduction_method(self, reduction_method):
        assert isinstance(reduction_method, ReductionMethod)
        self.reduction_method = reduction_method

    def set_peak_integration(self, peak_integration):
        assert isinstance(peak_integration, PeakIntegration)
        self.peak_integration = peak_integration

    def set_type(self, ch_type):
        assert isinstance(ch_type, str)
        self.type = ch_type
