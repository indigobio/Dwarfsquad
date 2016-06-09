from helpers import build_reference_map
import dwarfsquad.model


def build_compound_methods(compounds_csv):
    compound_methods = []
    for row in compounds_csv:
        try:
            compound_method = get_compound_method(compound_methods, row)
            chromatogram_method = get_chromatogram_method(row)
            compound_method.chromatogram_methods.append(chromatogram_method)
            compound_methods.insert(compound_method.view_order, compound_method)
        except Exception as e:
            for k, v in row.items():
                print(k + ": " + v)
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

    chromatogram_method = dwarfsquad.model.ChromatogramMethod({})
    chromatogram_method.set_peak_integration(get_peak_integration(row))
    chromatogram_method.set_reduction_method(get_reduction_method(row))
    chromatogram_method.set_name(row['chromatogram_name'])

    return chromatogram_method


def get_reduction_method(row):

    reduction_method = dwarfsquad.model.ReductionMethod({})
    reduction_method.set_activation_energy(row['activation_energy'])
    reduction_method.set_combine_ions(row['combine_ions'])
    reduction_method.set_lower_precursor_mass(row['lower_precursor_mass'])
    reduction_method.set_upper_precursor_mass(row['upper_precursor_mass'])
    reduction_method.set_lower_product_mass(row['lower_product_mass'])
    reduction_method.set_upper_product_mass(row['upper_product_mass'])
    reduction_method.set_polarity(row['polarity'])

    return reduction_method


def get_peak_integration(row):

    peak_integration = dwarfsquad.model.PeakIntegration({})
    peak_integration.set_retention_time(get_retention_time(row))
    peak_integration.set_threshold(get_threshold(row))
    peak_integration.set_smoothing(get_smoothing(row))
    peak_integration.set_prioritized_peak_models(get_prioritized_peak_models(row))

    return peak_integration


def get_prioritized_peak_models(row):

    return str(row['prioritized_peak_models']).split(';')


def get_smoothing(row):

    smoothing = dwarfsquad.model.Smoothing({})

    smoothing.set_fixed(row['fixed'])
    smoothing.set_max(row['max'])
    smoothing.set_min(row['min'])
    smoothing.set_optimal_enabled(row['optimal_enabled'])
    smoothing.set_start(row['start'])

    return smoothing


def get_threshold(row):

    threshold = dwarfsquad.model.Threshold({})
    threshold.set_peak_probability(row['peak_probability'])
    threshold.set_absolute_area(row['absolute_area'])
    threshold.set_absolute_height(row['absolute_height'])
    threshold.set_first_derivative(row['first_derivative'])
    threshold.set_second_derivative(row['second_derivative'])
    threshold.set_min_merge_difference(row['min_merge_difference'])
    threshold.set_relative_area(row['relative_area'])
    threshold.set_relative_height(row['relative_height'])
    threshold.set_saturation(row['saturation'])
    threshold.set_signal_to_noise(row['signal_to_noise'])

    return threshold


def get_retention_time(row):

    retention_time = dwarfsquad.model.RetentionTime({})
    retention_time.set_bias(row['bias'])
    retention_time.set_expected(row['expected'])
    retention_time.set_lower_tolerance(row['lower_tolerance'])
    retention_time.set_upper_tolerance(row['upper_tolerance'])
    retention_time.set_reference(row['reference'])
    retention_time.set_reference_type_source(row['reference_type_source'])
    retention_time.set_upper_trace_width(row['upper_trace_width'])
    retention_time.set_lower_trace_width(row['lower_trace_width'])
    retention_time.set_window_width(row['window_width'])
    retention_time.set_estimation_width(row['estimation_width'])

    return retention_time


def get_calibration(row):

    calibration = dwarfsquad.model.Calibration({})
    calibration.set_degree(row['degree'])
    calibration.set_enabled(row['enabled'])
    calibration.set_origin(row['origin'])
    calibration.set_weighting(row['weighting'])
    try:
        calibration.set_normalizers(str(row['normalizers']).split(';'))
    except ValueError:
        calibration.set_normalizers([])

    try:
        calibration.set_responses(str(row['responses']).split(';'))
    except ValueError:
        calibration.set_responses([])

    return calibration


def get_compound_method(cms, row):

    for index, cm in enumerate(cms):
        if row['compound_name'] == cm.name:
            return cms.pop(index)

    cm = dwarfsquad.model.CompoundMethod({})
    cm.set_name(row['compound_name'])
    cm.set_view_order(row['view_order'])
    cm.set_calibration(get_calibration(row))
    return cm