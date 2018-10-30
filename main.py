from machine import Memory, Accumulator, AddressRegister, DataRegister, InstructionRegister, ProgramCounter, \
    TemporaryRegister
import time


def wait():
    SLEEP_TIME = 0.1
    time.sleep(SLEEP_TIME)


def print_status(AC, AR, DR, IR, PC, TR):
    print("--------------")
    print(AC)
    print(AR)
    print(DR)
    print(IR)
    print(PC)
    print(TR)
    print("--------------")


def make_bin_lengthy(a, length):
    diff = length - len(a)
    for i in range(0, diff):
        a = '0' + a
    return a


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
    dr_value = DR.read()
    for char in dr_value:
        if char == '1':
            return False
    return True

def not_all_bits (reg) :
    not_reg = ''
    for bit in reg :
        if bit == '0' :
            not_reg.append('1')
        elif bit == '1' :
            not_reg.append('0')

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

    while True:
        wait()
        print("____STARTING____")

        # T0
        AR.write(PC.read())
        print_status(AC, AR, DR, IR, PC, TR)

        # T1
        PC.write(bin_add('1', PC.read()))
        IR.write(memory.memory[bin_to_decimal(AR.read())])
        print_status(AC, AR, DR, IR, PC, TR)

        # T2
        I = IR.read()[0]
        AR.write(IR.read()[4:16])
        D = bin_to_decimal(IR.read()[1:4])
        print_status(AC, AR, DR, IR, PC, TR)

        # T3
        if I == 1:
            AR.write(memory.memory[bin_to_decimal(AR.read())])

        if D == 0:
            # T4
            DR.write(memory.memory[bin_to_decimal(AR.read())])

            # T5
            AC.write(binary_and(AC.read(), DR.read()))

        elif D == 1:
            # T4
            DR.write(memory.memory[bin_to_decimal(AR.read())])

            # T5
            AC.write(bin_add(AC.read(), DR.read()))

        elif D == 2:
            # T4
            DR.write(memory.memory[bin_to_decimal(AR.read())])

            # T5
            AC.write(DR.read())

        elif D == 3:
            # T4
            memory.memory[bin_to_decimal(AR.read())] = AC.read()

        elif D == 4:
            # T4
            PC.write(AR.read())

        elif D == 5:
            # T4
            memory.memory[bin_to_decimal(AR.read())] = PC.read()
            AR.write(bin_add(AR.read(), '1'))

            # T5
            PC.write(AR.read())

        elif D == 6:
            # T4
            DR.write(memory.memory[bin_to_decimal(AR.read())])

            # T5
            DR.write(bin_add(DR.read(), '1'))

            # T6
            memory.memory[bin_to_decimal(AR.read())] = DR.read()
            if check_if_DR_is_zero():
                PC.write(bin_add(PC.read(), '1'))

        elif D == 7:
            B = bin_to_decimal(IR.read()[4:])
            E = IR.read()[0]
            if B == 0:
                pass
                # Change later
            elif B == 1:
                if E == 0:
                    PC.write(bin_add(PC.read(), '1'))
            elif B == 2:
                if bin_to_decimal(AC.read()) == 0:
                    PC.write(bin_add(PC.read(), '1'))

            elif B == 3:
                if AC.read()[0] == '1':
                    PC.write(bin_add(PC.read(), '1'))

            elif B == 4:
                if AC.read()[0] == '0':
                    PC.write(bin_add(PC.read(), '1'))

            elif B == 5:
                AC.write(bin_add(AC.read(), '1'))

            elif B == 6:
                pass

            elif B == 7:
                pass
            elif B == 8:
                if E == '1':
                    E = '0'
                else:
                    E = '1'
            elif E == 9 :


main()
# print(bin_add('0000011', '1'))
# a = "12345"
# print(a[1:2])
