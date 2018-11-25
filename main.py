from machine import *
import time

E_R = E_R()


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

                counter += 1

                B = bin_to_hex(IR.read())
                E = IR.read()[0]
                print("B : " + str(B))
                if B == "7001":
                    print("***** FINISHED *****")
                    break

                elif B == "7002":
                    if E == 0:
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
    except:
        pass


main()
