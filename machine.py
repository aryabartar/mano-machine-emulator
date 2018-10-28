def check_length(value, len):
    if not len(value) == len:
        raise Exception("No size match")


class Memory:
    memory = [0] * 4096

    def read(self, address):
        return self.memory[address]

    def write(self, address, input):
        self.memory[address] = input


class DataRegister:
    data = 0

    def read(self):
        return self.data

    def write(self, data):
        self.data = data


# accumulator remained

class InstructionRegister:
    instruction = ""

    def read(self):
        return self.instruction

    def write(self, instruction):
        self.instruction = instruction


class AddressRegister:
    address = ""

    def read(self):
        return self.address

    def write(self, value):
        check_length(value, 12)


class ProgramCounter:
    address = ""

    def read(self):
        if self.address == "":
            raise Exception("PC is empty!")
        return self.address

    def write(self, value):
        self.address = value
