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
    return result

def bin_to_decimal (binary_int) :
    return int(binary_int , 2)

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
        AR.write(PC.read())
        print_status(AC, AR, DR, IR, PC, TR)
        PC.write(bin_add('1', PC.read()))
        IR.write(memory.memory[bin_to_decimal(AR.read())])
        print_status(AC, AR, DR, IR, PC, TR)

main()
# print(bin_add('0000011', '1'))
