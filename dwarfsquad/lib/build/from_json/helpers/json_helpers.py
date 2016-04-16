from dwarfsquad.model import AssayConfiguration


def build_full_ac_from_json(json_doc):

    ac = AssayConfiguration(json_doc)
    set_references_to_id(ac)
    return ac


def set_references_to_id(ac):

    for idx, cm in enumerate(ac.compound_methods):

        cm.calibration.responses = [r.get("$oid") if isinstance(r, dict) else r for r in cm.calibration.responses]
        cm.calibration.normalizers = [n.get("$oid") if isinstance(n, dict) else n for n in cm.calibration.normalizers]

        for idy, ch_m in enumerate(cm.chromatogram_methods):
            if ch_m.peak_integration.retention_time.reference_type_source == 'chromatogram':
                ref = ch_m.peak_integration.retention_time.reference
                ch_m.peak_integration.retention_time.reference = ref.get("$oid") if isinstance(ref, dict) else ref