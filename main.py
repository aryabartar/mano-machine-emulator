def make_all_items_len_three(assembly_splitted_rows):
    for item in assembly_splitted_rows:
        if len(item) == 2:
            item.append('')


def read_from_input():
    assembly_raw_input = open("input.txt", "r")
    assembly_rows = assembly_raw_input.read().split("\n")
    assembly_splitted_rows = []
    for row in assembly_rows:
        assembly_splitted_rows.append(row.split(' '))
    make_all_items_len_three(assembly_splitted_rows)

    for item in assembly_splitted_rows:
        if not item[0] == '':
            if item[0][-1] == ',':
                item[0] = item[0][0:-1]
    return assembly_splitted_rows


def get_item_locations_as_dict(assembly_list):
    assembly_dict = {}
    LC = 0
    for item in assembly_list:
        if item[1] == "ORG":
            LC = int(item[2])
            continue
        assembly_dict[LC] = item
        LC += 1
    return assembly_dict


def replace_symbols_with_location(assembly_dict):
    def search_in_dict(search_key):
        for key, value in assembly_dict.items():
            if value[0] == search_key:
                return key

    for item in assembly_dict.values() :
        if not item[2] == '' :
            item[2] = search_in_dict(item[2])
    print(assembly_dict)

def handle_assembly_first_stage(assembly_list):
    """
    Creates location integer for symbols.
    :param assembly_list:
    :return:
    """
    assembly_dict = get_item_locations_as_dict(assembly_list)
    replace_symbols_with_location(assembly_dict)


assembly_list = read_from_input()
handle_assembly_first_stage(assembly_list)
# print(assembly_list)
