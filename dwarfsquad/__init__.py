from dwarfsquad.lib import actions
from dwarfsquad.lib import collections


def get_supported_actions():
    action_attr = dir(actions)
    items = []
    for attr in action_attr:
        if 'dwarf' not in attr and not attr.startswith('__'):
            items.append(attr.lower())

    return ' '.join(items)


def get_supported_collections():
    action_attr = dir(collections)
    items = []
    for attr in [attr for attr in action_attr if 'dwarf' not in attr and not attr.startswith('__')]:
        items.append(attr)

    return ' '.join(items)
