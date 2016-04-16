from BaseWebModel import BaseWebModel


class Calibration(BaseWebModel):
    required_fields = {
        "enabled": False,
        "degree": "linear",
        "weighting": "none",
        "origin": "ignore",
        "responses": [],
        "normalizers": []
    }

    @classmethod
    def __str__(cls):
        return "calibration"

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = dict(base.items() + arg.items())

        BaseWebModel.__init__(self, self.build_required_entities_only(base))

    def set_enabled(self, enabled):
        self.enabled = str(enabled).lower() == 'true'

    def set_degree(self, degree):
        try:
            assert isinstance(degree, basestring) and degree.lower() in ['linear', 'quadratic', 'cubic']
            self.degree = str(degree).lower()
        except AssertionError:
            self.degree = 'linear'

    def set_weighting(self, weighting):
        try:
            assert isinstance(weighting, basestring) and weighting.lower() in ['none', '1/x', '1/x2', '1/y', '1/y2']
            self.weighting = str(weighting).lower()
        except AssertionError:
            self.weighting = 'none'

    def set_origin(self, origin):
        try:
            assert isinstance(origin, basestring) and origin.lower() in ['ignore', 'include', 'force']
            self.origin = str(origin).lower()
        except AssertionError:
            self.origin = 'ignore'

    def set_responses(self, responses):
        assert isinstance(responses, list)
        self.responses = responses

    def set_normalizers(self, normalizers):
        assert isinstance(normalizers, list)
        self.normalizers = normalizers