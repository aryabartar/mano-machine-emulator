def read_from_input():
    assembly_raw_input = open("input.txt", "r")
    assembly_rows = assembly_raw_input.read().split("\n")
    assembly_splitted_rows = []
    for row in assembly_rows:
        assembly_splitted_rows.append(row.split(" "))
    return assembly_splitted_rows


def handle_assembly(assembly_list):
    def has_label(row_list):
        """
        :param row_list: Gets a row in form of splitted array.
        :return: True => if has label  | False => if not
        """
        if row_list[0][-1] == ",":
            return True
        return False

    for item in assembly_list:
        print(item[0])
        if not has_label(item) and item[0] == "LDA":
            print(item)


assembly_list = read_from_input()
handle_assembly(assembly_list)
