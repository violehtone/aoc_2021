def read_input_of_integers_to_list(file: str) -> list:
    """ Reads input like 123 to [123] """
    with open(file, 'r') as f:
        return [int(line.strip()) for line in f]


def read_input_to_list_of_tuples(file: str) -> list:
    """ Reads input like 'forward 2' to [('forward', '2')] """
    with open(file, 'r') as f:
        return [tuple(line.strip().split(" ")) for line in f]


def read_input_strings_to_list(file: str) -> list:
    """ Reads input like abcd" to ["abcd"] """
    with open(file, 'r') as f:
        return [(line.strip()) for line in f]
