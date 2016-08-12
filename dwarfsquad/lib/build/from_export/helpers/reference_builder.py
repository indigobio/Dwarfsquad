def build_reference_map(cms):

    reference_map = {'': ''}
    for cm in cms:
        for ch_m in cm.chromatogram_methods:
            reference_map[str(ch_m.id)] = cm.name + ' - ' + ch_m.name
            reference_map[ch_m.id] = cm.name + ' - ' + ch_m.name
            reference_map[cm.name + ' - ' + ch_m.name] = str(ch_m.id)
    return reference_map
