def check_length(value, length):
    if not len(value) == length:
        raise Exception("No size match")


def if_empty_raise_exception(string):
    if string == "":
        raise Exception("Register string is EMPTY!")


class Memory:
    memory = [0] * 4096

    def read(self, address):
        return self.memory[address]

    def write(self, address, input):
        self.memory[address] = input

    def __str__(self):
        return self.memory


class DataRegister:
    data = ""

    def read(self):
        return self.data

    def write(self, data):
        check_length(data, 16)
        self.data = data

    def __str__(self):
        return "DR: " + self.data


class InstructionRegister:
    instruction = ""

    def read(self):
        return self.instruction

    def write(self, instruction):
        check_length(instruction, 16)
        self.instruction = instruction

    def __str__(self):
        return "IR: " + self.instruction


class AddressRegister:
    address = ""

    def read(self):
        return self.address

    def write(self, address):
        check_length(address, 12)
        self.address = address

    def __str__(self):
        return "AR: " + self.address


class ProgramCounter:
    address = "000000000000"

    def read(self):
        if_empty_raise_exception(self.address)
        return self.address

    def write(self, value):
        check_length(value, 12)
        self.address = value

    def __str__(self):
        return "PC: " + self.address


class Accumulator:
    data = ""

    def read(self):
        if_empty_raise_exception(self.data)
        return self.data

    def write(self, data):
        check_length(data, 16)
        self.data = data

    def __str__(self):
        return "AC: " + self.data


class TemporaryRegister:
    data = ""

    def read(self):
        if_empty_raise_exception(self.data)
        return self.data

    def write(self, data):
        check_length(data, 16)
        self.data = data

    def __str__(self):
        return "TR: " + self.data
