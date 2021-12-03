from utils import read_input_to_list_of_tuples


def part1(coordinates: list) -> None:
    """ Answer to part 1 """
    horizontal_position = 0
    depth = 0

    for coordinate in coordinates:
        if coordinate[0] == "forward":
            horizontal_position += int(coordinate[1])
        elif coordinate[0] == "up":
            depth -= int(coordinate[1])
        elif coordinate[0] == "down":
            depth += int(coordinate[1])
    return print(f"Result to part 1: {depth*horizontal_position}")


def part2(coordinates: list) -> None:
    """ Answer to part 2 """
    horizontal_position = 0
    depth = 0
    aim = 0

    for coordinate in coordinates:
        if coordinate[0] == "forward":
            horizontal_position += int(coordinate[1])
            depth += (aim * int(coordinate[1]))
        elif coordinate[0] == "up":
            aim -= int(coordinate[1])
        elif coordinate[0] == "down":
            aim += int(coordinate[1])
    return print(f"Result to part 2: {depth*horizontal_position}")


if __name__ == "__main__":
    coordinates = read_input_to_list_of_tuples(file="input_data/day2.txt")
    part1(coordinates=coordinates)
    part2(coordinates=coordinates)
