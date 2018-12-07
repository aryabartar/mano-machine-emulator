<<<<<<< HEAD
from machine import *

E_R = E_R()


def wait():
    pass

def print_status(AC, AR, DR, IR, PC, TR):
    print("--------------")
    print(AC)
    print(AR)
    print(DR)
    print(IR)
    print(PC)
    print(TR)
    print("E_R:" + E_R.read())
    print("--------------")


def make_bin_lengthy(a, length):
    diff = length - len(a)
    for i in range(0, diff):
        a = '0' + a
    return a


def bin_to_hex(number):
    return hex(int(str(number), 2))[2:]


def bin_add(a, b):
    bin_result = bin(int(a, 2) + int(b, 2))
    result = make_bin_lengthy(bin_result[2:], max(len(a), len(b)))
    if len(result) > max(len(a), len(b)):
        result = result[1:]
    return result


def bin_to_decimal(binary_int):
    return int(binary_int, 2)


def binary_and(a, b):
    if not len(a) == len(b):
        raise Exception("Lengths are not equal!!")
    temp_bin = ""
    for i in range(0, len(a)):
        if a[i] == '1' and b[i] == '1':
            temp_bin += '1'
        else:
            temp_bin += '0'
    return temp_bin


def check_if_DR_is_zero(DR):
    print("-------")
    dr_value = DR.read()
    for char in dr_value:
        if char == '1':
            return False
    return True


def not_all_bits(reg):
    not_reg = ""
    for bit in reg:
        if bit == '0':
            not_reg += '1'
        elif bit == '1':
            not_reg += '0'

    return not_reg


def main():
    memory = Memory()
    AC = Accumulator()
    AR = AddressRegister()
    DR = DataRegister()
    IR = InstructionRegister()
    PC = ProgramCounter()
    TR = TemporaryRegister()

    f = open("input.txt", "r")
    memory.memory = f.read().split("\n")

    try:
        total_counter = 0
        while True:
            counter = 0
            wait()
            print("STARTING...")

            # T0
            AR.write(PC.read())
            counter += 1

            # T1
            PC.write(bin_add('1', PC.read()))
            IR.write(memory.memory[bin_to_decimal(AR.read())])
            counter += 1

            print("READING : " + IR.read())
            # T2
            I = IR.read()[0]
            AR.write(IR.read()[4:16])
            D = bin_to_decimal(IR.read()[1:4])
            counter += 1

            # T3
            if I == 1:
                AR.write(memory.memory[bin_to_decimal(AR.read())])
            counter += 1

            if D == 0:
                print("D0")
                # T4
                DR.write(memory.memory[bin_to_decimal(AR.read())])
                counter += 1

                # T5
                AC.write(binary_and(AC.read(), DR.read()))
                counter += 1


            elif D == 1:
                print("D1")

                # T4
                DR.write(memory.memory[bin_to_decimal(AR.read())])
                counter += 1

                # T5
                AC.write(bin_add(AC.read(), DR.read()))
                counter += 1


            elif D == 2:
                print("D2")

                # T4
                DR.write(memory.memory[bin_to_decimal(AR.read())])
                counter += 1

                # T5
                AC.write(DR.read())
                counter += 1


            elif D == 3:
                print("D3")

                # T4
                memory.memory[bin_to_decimal(AR.read())] = AC.read()
                counter += 1


            elif D == 4:
                print("D4")

                # T4
                PC.write(AR.read())
                counter += 1


            elif D == 5:
                print("D5")

                # T4
                memory.memory[bin_to_decimal(AR.read())] = PC.read()
                AR.write(bin_add(AR.read(), '1'))
                counter += 1

                # T5
                PC.write(AR.read())
                counter += 1


            elif D == 6:
                print("D6")

                # T4
                DR.write(memory.memory[bin_to_decimal(AR.read())])
                counter += 1
                print("T4")

                # T5
                DR.write(bin_add(DR.read(), '1'))
                counter += 1
                print("T5")

                # T6
                memory.memory[bin_to_decimal(AR.read())] = DR.read()
                if check_if_DR_is_zero(DR):
                    PC.write(bin_add(PC.read(), '1'))

                counter += 1
                print("T6")


            elif D == 7:
                print("D7")

                B = bin_to_hex(IR.read())
                print("B : " + str(B))
                if B == "7001":
                    temp_ctr = 0
                    for item in memory.memory:
                        print(temp_ctr)
                        print(item)
                        temp_ctr += 1
                    print("***** FINISHED *****")
                    break

                elif B == "7002":
                    if E_R.read() == '0':
                        PC.write(bin_add(PC.read(), '1'))

                elif B == "7004":
                    if bin_to_decimal(AC.read()) == 0:
                        PC.write(bin_add(PC.read(), '1'))

                elif B == "7008":
                    if AC.read()[0] == '1':
                        PC.write(bin_add(PC.read(), '1'))

                elif B == "7010":
                    if AC.read()[0] == '0':
                        PC.write(bin_add(PC.read(), '1'))

                elif B == "7020":
                    AC.write(bin_add(AC.read(), '1'))

                elif B == "7040":
                    temp_E_R = AC.read()[0]
                    AC.write(AC.read()[1:] + E_R.read())
                    E_R.write(temp_E_R)

                elif B == "7080":
                    temp_E_R = AC.read()[15]
                    AC.write(E_R.read() + AC.read()[0: 15])
                    E_R.write(temp_E_R)

                elif B == "7100":
                    if E_R.read() == '0':
                        E_R.write('1')
                    else:
                        E_R.write('0')

                elif B == "7200":
                    AC.write(not_all_bits(AC.read()))

                elif B == "7400":
                    E_R.write('0')

                elif B == "7800":
                    AC.write('0000000000000000')

            print_status(AC, AR, DR, IR, PC, TR)
            print("Clock counter : " + str(counter))
            total_counter += counter
            print("Total counter : " + str(total_counter))

    except:
        pass


main()
=======
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
    return hex_list


def hex_to_bin(hex_num):
    def make_size_16(num):
        num = str(num)
        num = '0' * (16 - len(num)) + num
        return num

    scale = 16  ## equals to hexadecimal
    num_of_bits = 8
    return make_size_16(bin(int(hex_num, scale))[2:].zfill(num_of_bits))


def final_write_hex(hex_list):
    f = open("output-hex.txt", "w")
    for item in hex_list:
        f.write(item + "\n")


def final_write_bin(hex_list):
    f = open("output-bin.txt", "w")
    for item in hex_list:
        f.write(hex_to_bin(item) + "\n")


assembly_list = read_from_input()
assembly_dict = handle_assembly_first_stage(assembly_list)
hex_list = handle_assembly_second_stage(assembly_dict)
final_write_hex(hex_list)
final_write_bin(hex_list)
>>>>>>> assembly-to-binary/master
