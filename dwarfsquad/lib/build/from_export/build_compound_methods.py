from dwarfsquad.lib.build.from_export.helpers import build_reference_map
from dwarfsquad.lib.utils import to_stderr
from dwarfsquad.model.Calibration import Calibration
from dwarfsquad.model.ChromatogramMethod import ChromatogramMethod
from dwarfsquad.model.CompoundMethod import CompoundMethod
from dwarfsquad.model.PeakIntegration import PeakIntegration
from dwarfsquad.model.ReductionMethod import ReductionMethod
from dwarfsquad.model.RetentionTime import RetentionTime
from dwarfsquad.model.Smoothing import Smoothing
from dwarfsquad.model.Threshold import Threshold


def build_compound_methods(compounds_csv):
    compound_methods = []
    unique_compound_choromatograms = set()
    for row in compounds_csv:
        try:
            compound_method = get_compound_method(compound_methods, row)
            chromatogram_method = get_chromatogram_method(row)
            compound_method.chromatogram_methods.append(chromatogram_method)
            compound_methods.insert(compound_method.view_order, compound_method)
            unique_compound_chromatogram_name = compound_method.name + " - " + chromatogram_method.name
            if unique_compound_chromatogram_name in unique_compound_choromatograms:
                raise Exception("Assay already contains a compound/chromatogram combo of: " +
                                unique_compound_chromatogram_name)
            else:
                unique_compound_choromatograms.add(unique_compound_chromatogram_name)
        except Exception as e:
            for k, v in row.items():
                to_stderr(k + ": " + v)
            raise e

    reference_map = build_reference_map(compound_methods)
    return resolve_references(compound_methods, reference_map)


def resolve_references(compound_methods, reference_map):
    resolved_cms = []
    for cm in compound_methods:
        cm.calibration.normalizers = [reference_map[n] for n in cm.calibration.normalizers if n]
        cm.calibration.responses = [reference_map[r] for r in cm.calibration.responses if r]
        resolved_ch_ms = []
        for ch_m in cm.chromatogram_methods:
            try:
                reference = ch_m.peak_integration.retention_time.reference
                ch_m.peak_integration.retention_time.reference = reference_map[reference]
            except KeyError:
                pass
            resolved_ch_ms.append(ch_m)
        cm.chromatogram_methods = resolved_ch_ms
        resolved_cms.append(cm)
    return resolved_cms


def get_chromatogram_method(row):

    chromatogram_method = ChromatogramMethod({})
    chromatogram_method.set_peak_integration(get_peak_integration(row))
    chromatogram_method.set_reduction_method(get_reduction_method(row))
    chromatogram_method.set_name(row.get('chromatogram_name'))

    return chromatogram_method


def get_reduction_method(row):

    reduction_method = ReductionMethod({})
    reduction_method.set_activation_energy(row.get('activation_energy'))
    reduction_method.set_combine_ions(row.get('combine_ions'))
    reduction_method.set_lower_precursor_mass(row.get('lower_precursor_mass'))
    reduction_method.set_upper_precursor_mass(row.get('upper_precursor_mass'))
    reduction_method.set_lower_product_mass(row.get('lower_product_mass'))
    reduction_method.set_upper_product_mass(row.get('upper_product_mass'))
    reduction_method.set_polarity(row.get('polarity'))

    return reduction_method


def get_peak_integration(row):

    peak_integration = PeakIntegration({})
    peak_integration.set_retention_time(get_retention_time(row))
    peak_integration.set_threshold(get_threshold(row))
    peak_integration.set_smoothing(get_smoothing(row))
    peak_integration.set_prioritized_peak_models(get_prioritized_peak_models(row))

    return peak_integration


def get_prioritized_peak_models(row):

    return str(row.get('prioritized_peak_models')).split(';')


def get_smoothing(row):

    smoothing = Smoothing({})

    smoothing.set_fixed(row.get('fixed'))
    smoothing.set_max(row.get('max'))
    smoothing.set_min(row.get('min'))
    smoothing.set_optimal_enabled(row.get('optimal_enabled'))
    smoothing.set_start(row.get('start'))

    return smoothing


def get_threshold(row):

    threshold = Threshold({})
    threshold.set_peak_probability(row.get('peak_probability'))
    threshold.set_absolute_area(row.get('absolute_area'))
    threshold.set_absolute_height(row.get('absolute_height'))
    threshold.set_first_derivative(row.get('first_derivative'))
    threshold.set_second_derivative(row.get('second_derivative'))
    threshold.set_min_merge_difference(row.get('min_merge_difference'))
    threshold.set_relative_area(row.get('relative_area'))
    threshold.set_relative_height(row.get('relative_height'))
    threshold.set_saturation(row.get('saturation'))
    threshold.set_signal_to_noise(row.get('signal_to_noise'))

    return threshold


def get_retention_time(row):

    retention_time = RetentionTime({})
    retention_time.set_bias(row.get('bias'))
    retention_time.set_expected(row.get('expected'))
    retention_time.set_lower_tolerance(row.get('lower_tolerance'))
    retention_time.set_upper_tolerance(row.get('upper_tolerance'))
    retention_time.set_reference(row.get('reference'))
    retention_time.set_reference_type_source(row.get('reference_type_source'))
    retention_time.set_upper_trace_width(row.get('upper_trace_width'))
    retention_time.set_lower_trace_width(row.get('lower_trace_width'))
    retention_time.set_window_width(row.get('window_width'))
    retention_time.set_estimation_width(row.get('estimation_width'))
    retention_time.set_window_multiplier(row.get('window_multiplier'))

    return retention_time


def get_calibration(row):

    calibration = Calibration({})
    calibration.set_degree(row.get('degree'))
    calibration.set_enabled(row.get('enabled'))
    calibration.set_origin(row.get('origin'))
    calibration.set_weighting(row.get('weighting'))
    try:
        calibration.set_normalizers(str(row.get('normalizers')).split(';'))
    except ValueError:
        calibration.set_normalizers([])

    try:
        calibration.set_responses(str(row.get('responses')).split(';'))
    except ValueError:
        calibration.set_responses([])

    return calibration


def get_compound_method(cms, row):

    for index, cm in enumerate(cms):
        if row.get('compound_name') == cm.name:
            return cms.pop(index)

    cm = CompoundMethod({})
    cm.set_name(row.get('compound_name'))
    cm.set_view_order(row.get('view_order'))
    cm.set_calibration(get_calibration(row))
    return cm
