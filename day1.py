from utils import read_input_of_integers_to_list


def part1(input_data: list):
    """ Answer to part 1 """
    result = 0
    for i in range(1, len(input_data)):
        if input_data[i] > input_data[i-1]:
            result += 1

    print(f"Result to part 1: {result}")


def part2(input_data: list):
    """ Answer to part 2 """
    result = 0
    windows = [input_data[i:i+3] for i in range(0, len(input_data))]
    for i in range(1, len(windows)):
        if sum(windows[i]) > sum(windows[i-1]):
            result += 1

    print(f"Result to part 2: {result}")


if __name__ == "__main__":
    input_data = read_input_of_integers_to_list('input_data/day1.txt')
    part1(input_data=input_data)
    part2(input_data=input_data)
