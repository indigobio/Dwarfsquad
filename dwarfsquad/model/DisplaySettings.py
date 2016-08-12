from dwarfsquad.model.BaseWebModel import BaseWebModel


class DisplaySettings(BaseWebModel):

    required_fields = {
        'peak_area_format': 'decimal_format',
        'concentration_format': 'decimal_format',
        'response_format': 'decimal_format',
        'review_method': 'index'
    }

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = {**base, **arg}
        BaseWebModel.__init__(self, self.build_required_entities_only(base))

    def set_peak_area_format(self, peak_area_format):
        if peak_area_format in ['decimal_format', 'scientific_notation']:
            self.peak_area_format = peak_area_format
        else:
            self.peak_area_format = 'decimal_format'

    def set_concentration_format(self, concentration_format):
        if concentration_format in ['decimal_format', 'scientific_notation']:
            self.concentration_format = concentration_format
        else:
            self.concentration_format = 'decimal_format'

    def set_response_format(self, response_format):
        if response_format in ['decimal_format', 'scientific_notation']:
            self.response_format = response_format
        else:
            self.response_format = 'decimal_format'

    def set_review_method(self, review_method):
        if review_method in ['index', 'analyte', 'type']:
            self.review_method = review_method
        else:
            self.review_method = 'index'
