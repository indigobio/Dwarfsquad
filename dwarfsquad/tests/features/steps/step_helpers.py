def find_item_in_list_by_name(items, name):

    if isinstance(items, list):
        for item in items:
            if item.get('name') == name:
                return item
    elif isinstance(items, dict):
        if items.get('name') == name:
            return items

    raise AssertionError