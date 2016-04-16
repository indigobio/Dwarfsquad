from BaseWebModel import BaseWebModel
from RetentionTime import RetentionTime
from Smoothing import Smoothing
from Threshold import Threshold


class PeakIntegration(BaseWebModel):
    required_fields = {
        "prioritized_peak_models": [
            "emg",
            "gaussian",
            "simpson"],
        "retention_time": RetentionTime({}),
        "threshold": Threshold({}),
        "smoothing": Smoothing({})
    }

    @classmethod
    def __str__(cls):
        return "peak integration"

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = dict(base.items() + arg.items())

        BaseWebModel.__init__(self, self.build_required_entities_only(base))

        self.set_retention_time(RetentionTime(self.retention_time))
        self.set_threshold(Threshold(self.threshold))
        self.set_smoothing(Smoothing(self.smoothing))

    def set_prioritized_peak_models(self, prioritized_peak_models):
        assert isinstance(prioritized_peak_models, list)
        self.prioritized_peak_models = prioritized_peak_models

    def set_retention_time(self, retention_time):
        assert isinstance(retention_time, RetentionTime)
        self.retention_time = retention_time

    def set_threshold(self, threshold):
        assert isinstance(threshold, Threshold)
        self.threshold = threshold

    def set_smoothing(self, smoothing):
        assert isinstance(smoothing, Smoothing)
        self.smoothing = smoothing