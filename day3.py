from utils import read_input_strings_to_list


def multiply_binary_strings(str1: str, str2: str) -> int:
    return int(str1, 2) * int(str2, 2)


def get_most_common_binary(mylist: list) -> str:
    if mylist.count("1") == mylist.count("0"):
        return "1"
    else:
        return max(set(mylist), key=mylist.count)


def get_least_common_binary(mylist: list) -> str:
    if mylist.count("1") == mylist.count("0"):
        return "0"
    else:
        return min(set(mylist), key=mylist.count)


def get_rating(diagnostic_report: list, func) -> str:
    """
    Get the rating as a binary string.
    func = either get_most_common_binary() or get_least_common_binary()
    """
    for i in range(0, len(diagnostic_report[0])):
        column_i = [item[i] for item in diagnostic_report]
        number_to_keep = func(column_i)
        indexes = [j for j in range(0, len(column_i)) if column_i[j] == number_to_keep]
        diagnostic_report = [diagnostic_report[x] for x in indexes]
        if len(diagnostic_report) == 1:
            return(diagnostic_report[0])


def part1(diagnostic_report: list):
    """ Answer to part 1 """
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(0, len(diagnostic_report[0])):
        column_i = [item[i] for item in diagnostic_report]
        gamma_rate += get_most_common_binary(column_i)
        epsilon_rate += get_least_common_binary(column_i)

    print(multiply_binary_strings(
        str1=gamma_rate,
        str2=epsilon_rate
    ))


def part2(diagnostic_report: list):
    """ Answer to part2 """
    oxygen_rating = get_rating(
        diagnostic_report=diagnostic_report,
        func=get_most_common_binary
    )
    co2_rating = get_rating(
        diagnostic_report=diagnostic_report,
        func=get_least_common_binary
    )
    print(multiply_binary_strings(
        str1=oxygen_rating,
        str2=co2_rating
    ))


if __name__ == "__main__":
    diagnostic_report = read_input_strings_to_list("input_data/day3.txt")
    part1(diagnostic_report=diagnostic_report)
    part2(diagnostic_report=diagnostic_report)
