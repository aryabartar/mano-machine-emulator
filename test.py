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


