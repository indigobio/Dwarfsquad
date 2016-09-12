import csv
from tqdm import tqdm
from collections import OrderedDict
from dwarfsquad.lib.utils import to_stderr, map_chromatogram_methods
from dwarfsquad.model.AssayConfiguration import AssayConfiguration
from dwarfsquad.lib.build.from_export import helpers as export_helpers


def export_compounds(ac):

    assert isinstance(ac, AssayConfiguration)
    rows = build_compound_rows(ac)
    with open('compounds.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
        to_stderr("Wrote compound and chromatogram methods to compounds.csv!")


def build_compound_rows(ac):
    rows = []
    reference_map = export_helpers.build_reference_map(ac.compound_methods)
    for compound in tqdm(ac.compound_methods, leave=True):
        rows.extend(build_compound_row(compound, reference_map))
    rows = sorted(rows, key=lambda k: k['view_order'])
    return rows


def build_compound_row(compound, reference_map):
    """ @type compound: CompoundMethod.CompoundMethod """

    rows = []
    for ch_m in compound.chromatogram_methods:
        row = OrderedDict()
        row['view_order'] = compound.view_order
        row['compound_name'] = compound.name
        row['chromatogram_name'] = ch_m.name
        row['lower_precursor_mass'] = ch_m.reduction_method.lower_precursor_mass
        row['upper_precursor_mass'] = ch_m.reduction_method.upper_precursor_mass
        row['lower_product_mass'] = ch_m.reduction_method.lower_product_mass
        row['upper_product_mass'] = ch_m.reduction_method.upper_product_mass
        row['expected'] = ch_m.peak_integration.retention_time.expected
        try:
            row['reference'] = reference_map[ch_m.peak_integration.retention_time.reference]
        except KeyError:
            row['reference'] = ch_m.peak_integration.retention_time.reference
        row['bias'] = ch_m.peak_integration.retention_time.bias
        row['lower_tolerance'] = ch_m.peak_integration.retention_time.lower_tolerance
        row['upper_tolerance'] = ch_m.peak_integration.retention_time.upper_tolerance
        row['origin'] = compound.calibration.origin
        row['weighting'] = compound.calibration.weighting
        row['enabled'] = str(compound.calibration.enabled)
        row['degree'] = compound.calibration.degree
        row['responses'] = ';'.join(map_chromatogram_methods(reference_map, compound.calibration.responses))
        row['normalizers'] = ';'.join(map_chromatogram_methods(reference_map, compound.calibration.normalizers))
        row['polarity'] = ch_m.reduction_method.polarity
        row['combine_ions'] = str(ch_m.reduction_method.combine_ions)
        row['activation_energy'] = ch_m.reduction_method.activation_energy
        row['window_width'] = ch_m.peak_integration.retention_time.window_width
        row['estimation_width'] = ch_m.peak_integration.retention_time.estimation_width
        row['reference_type_source'] = ch_m.peak_integration.retention_time.reference_type_source
        row['lower_trace_width'] = ch_m.peak_integration.retention_time.lower_trace_width
        row['upper_trace_width'] = ch_m.peak_integration.retention_time.upper_trace_width
        row['max'] = ch_m.peak_integration.smoothing.max
        row['min'] = ch_m.peak_integration.smoothing.min
        row['optimal_enabled'] = str(ch_m.peak_integration.smoothing.optimal_enabled)
        row['start'] = ch_m.peak_integration.smoothing.start
        row['fixed'] = ch_m.peak_integration.smoothing.fixed
        row['saturation'] = ch_m.peak_integration.threshold.saturation
        row['min_merge_difference'] = ch_m.peak_integration.threshold.min_merge_difference
        row['peak_probability'] = ch_m.peak_integration.threshold.peak_probability
        row['absolute_area'] = ch_m.peak_integration.threshold.absolute_area
        row['relative_area'] = ch_m.peak_integration.threshold.relative_area
        row['absolute_height'] = ch_m.peak_integration.threshold.absolute_height
        row['relative_height'] = ch_m.peak_integration.threshold.relative_height
        row['signal_to_noise'] = ch_m.peak_integration.threshold.signal_to_noise
        row['first_derivative'] = ch_m.peak_integration.threshold.first_derivative
        row['second_derivative'] = ch_m.peak_integration.threshold.second_derivative
        row['prioritized_peak_models'] = ';'.join(ch_m.peak_integration.prioritized_peak_models)

        rows.append(row)

    return rows
