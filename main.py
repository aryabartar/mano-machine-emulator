FUNC_HEX = {
    "AND": "0",
    "ANDI": "8",
    "ADD": "1",
    "ADDI": "9",
    "LDA": "2",
    "LDAI": "A",
    "STA": "3",
    "STAI": "B",
    "BUN": "4",
    "BUNI": "C",
    "BSA": "4",
    "BSAI": "D",
    "ISZ": "6",
    "ISZI": "E",

    "CLA": "7800",
    "CLE": "7400",
    "CMA": "7200",
    "CME": "7100",
    "CIR": "7080",
    "CIL": "7040",
    "INC": "7020",
    "SPA": "7010",
    "SNA": "7008",
    "SZA": "7004",
    "SZE": "7002",
    "HLT": "7001",

    "INP": "F800",
    "OUT": "F400",
    "SKI": "F200",
    "SKO": "F100",
    "ION": "F080",
    "IOF": "F040",

}


def hex_to_dec(hex_number):
    return int(str(hex_number), 16)


def make_all_items_len_three(assembly_splitted_rows):
    for item in assembly_splitted_rows:
        if len(item) == 2:
            item.append('')


def complement_hex(decimal_number):
    binary = str(bin(int(decimal_number)))[2:]
    binary = ('0' * (16 - len(binary))) + binary
    comp_bin = ''
    for i in binary:
        if i == '0':
            comp_bin += '1'
        else:
            comp_bin += '0'

    return hex(int(comp_bin, 2) + int('1', 2))[2:]


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
            LC = hex_to_dec(item[2])
            continue
        assembly_dict[LC] = item
        LC += 1
    return assembly_dict


def replace_symbols_with_location(assembly_dict):
    def search_in_dict(search_key):
        for key, value in assembly_dict.items():
            if value[0] == search_key:
                return key

    for item in assembly_dict.values():
        if not (item[1] == 'HEX' or item[1] == 'DEC'):
            if not item[2] == '':
                if item[-1] == 'I':
                    item[2] = assembly_dict[search_in_dict(item[2])][2]
                    pass
                else:
                    item[2] = search_in_dict(item[2])

    return assembly_dict


def change_hex_with_dec_in_dict(assembly_dict):
    for item in assembly_dict.values():
        if item[1] == "HEX":
            item[1] = "DEC"
            item[2] = hex_to_dec(item[2])
    return assembly_dict


def handle_assembly_first_stage(assembly_list):
    """
    Creates location integer for symbols.
    :param assembly_list:
    :return:
    """
    assembly_dict = get_item_locations_as_dict(assembly_list)
    assembly_dict = change_hex_with_dec_in_dict(assembly_dict)
    return replace_symbols_with_location(assembly_dict)


def make_hex_size_4(hex_number):
    for i in range(len(hex_number), 4):
        hex_number = '0' + hex_number
    return hex_number


def dec_to_hex(decimal_number):
    if str(decimal_number)[0] == '-':
        hex_number = complement_hex(str(decimal_number)[1:])
    else:
        hex_number = hex(int(decimal_number)).split('x')[-1]
    return make_hex_size_4(hex_number.upper())


def handle_assembly_second_stage(assembly_dict):
    hex_list = []
    for item in assembly_dict.values():
        # IF for END,  ORG,
        if not (item[1] == 'END' or item[1] == 'ORG' or item[1] == 'DEC' or item[1] == 'HEX'):
            if item[2] == '':
                hex_list.append(FUNC_HEX[item[1]])
            elif not item[2] == '':
                hex_list.append(FUNC_HEX[item[1]] + str(dec_to_hex(item[2]))[1:])
        elif item[1] == 'HEX' or item[1] == 'DEC':
            if item[1] == 'HEX':
                hex_list.append(str(make_hex_size_4(item[2])))
            elif item[1] == 'DEC':
                hex_list.append(str(dec_to_hex(item[2])))
    print(hex_list)


assembly_list = read_from_input()
assembly_dict = handle_assembly_first_stage(assembly_list)
print(assembly_dict)
handle_assembly_second_stage(assembly_dict)
print(dec_to_hex("-8"))
