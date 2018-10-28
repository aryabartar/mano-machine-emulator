from machine import Memory, Accumulator, AddressRegister, DataRegister, InstructionRegister, ProgramCounter, \
    TemporaryRegister


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
        AR.write(PC.read())


main()
