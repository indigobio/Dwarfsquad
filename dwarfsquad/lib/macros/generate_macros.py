from dwarfsquad.lib.build.from_export.helpers import build_reference_map


def generate_macros(ac):
    macros = []
    reference_map = build_reference_map(ac.compound_methods)
    for cm in ac.compound_methods:
        for normalizer in cm.calibration.normalizers:
            relate = "relate " + cm.name + " " + reference_map[normalizer].split(" ")[0]
            if relate not in macros:
                macros.append(relate)

        for ch_m in cm.chromatogram_methods:
            rt = ch_m.peak_integration.retention_time
            if rt.reference_type_source == "chromatogram":
                relate = "relate " + cm.name + " " + reference_map[rt.reference].split(" ")[0]
                if relate not in macros:
                    macros.append(relate)
    return macros
