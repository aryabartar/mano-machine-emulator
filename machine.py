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

    def write(self, data) :
        self.data = data

