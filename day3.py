"""day3"""


def read_input(filepath):
    numbers = list()
    with open(filepath, "r") as f:
        for line in f:
            numbers.append(line)
    return numbers


def day3_part1():
    """part1"""
    input_list = read_input("aoc2023\input3.txt")
    input_list_itterator = iter(input_list)

    next_line = list(next(input_list_itterator))
    line_1 = next_line
    next_line = list(next(input_list_itterator))
    line_2 = next_line
    next_line = list(next(input_list_itterator))

    result = 0

    while (True):
        line_3 = next_line
        for element in range(1, len(line_2)-1):
            if (line_2[element] != '.') and not (line_2[element].isdigit()):
                if line_1[element].isdigit():
                    # print("above")
                    number = get_number_replace_with_dot(line_1, element)
                    result = result + int(number)
                if line_1[element-1].isdigit():
                    # print("aboveLeft")
                    number = get_number_replace_with_dot(line_1, element-1)
                    result = result + int(number)
                if line_1[element+1].isdigit():
                    # print("aboveRight")
                    number = get_number_replace_with_dot(line_1, element+1)
                    result = result + int(number)
                if line_2[element-1].isdigit():
                    # print("Left")
                    number = get_number_replace_with_dot(line_2, element-1)
                    result = result + int(number)
                if line_2[element+1].isdigit():
                    # print("Right")
                    number = get_number_replace_with_dot(line_2, element+1)
                    result = result + int(number)
                if line_3[element].isdigit():
                    # print("below")
                    number = get_number_replace_with_dot(line_3, element)
                    result = result + int(number)
                if line_3[element-1].isdigit():
                    # print("belowLeft")
                    number = get_number_replace_with_dot(line_3, element-1)
                    result = result + int(number)
                if line_3[element+1].isdigit():
                    # print("belowRight")
                    number = get_number_replace_with_dot(line_3, element+1)
                    result = result + int(number)

        try:
            next_line = list(next(input_list_itterator))
        except:
            break

        line_1 = line_2
        line_2 = line_3

    return result


def get_number_replace_with_dot(line: list, element: int):
    """get_number_replace_with_dot"""
    number = line[element]
    line[element] = '.'
    start_index = element - 1
    while line[start_index].isdigit():
        number = line[start_index] + number
        line[start_index] = '.'
        start_index = start_index - 1
    end_index = element + 1
    while line[end_index].isdigit():
        number = number + line[end_index]
        line[end_index] = '.'
        end_index = end_index + 1

    return number


def day3_part2():
    """part2"""
    input_list = read_input("aoc2023\input3.txt")
    input_list_itterator = iter(input_list)

    next_line = list(next(input_list_itterator))
    line_1 = next_line
    next_line = list(next(input_list_itterator))
    line_2 = next_line
    next_line = list(next(input_list_itterator))

    result = 0

    while True:
        line_3 = next_line
        for element in range(1, len(line_2)-1):

            if line_2[element] == '*':
                gear_ratio = 1
                gear_limit = 0
                if line_1[element].isdigit():
                    # print("above")
                    number = get_number_replace_with_dot(line_1, element)
                    if gear_limit > 2:
                        continue
                    gear_ratio = gear_ratio * int(number)
                    gear_limit = gear_limit + 1
                if line_1[element-1].isdigit():
                    # print("aboveLeft")
                    number = get_number_replace_with_dot(line_1, element-1)
                    if gear_limit > 2:
                        continue
                    gear_ratio = gear_ratio * int(number)
                    gear_limit = gear_limit + 1
                if line_1[element+1].isdigit():
                    # print("aboveRight")
                    number = get_number_replace_with_dot(line_1, element+1)
                    if gear_limit > 2:
                        continue
                    gear_ratio = gear_ratio * int(number)
                    gear_limit = gear_limit + 1
                if line_2[element-1].isdigit():
                    # print("Left")
                    number = get_number_replace_with_dot(line_2, element-1)
                    if gear_limit > 2:
                        continue
                    gear_ratio = gear_ratio * int(number)
                    gear_limit = gear_limit + 1
                if line_2[element+1].isdigit():
                    # print("Right")
                    number = get_number_replace_with_dot(line_2, element+1)
                    if gear_limit > 2:
                        continue
                    gear_ratio = gear_ratio * int(number)
                    gear_limit = gear_limit + 1
                if line_3[element].isdigit():
                    # print("below")
                    number = get_number_replace_with_dot(line_3, element)
                    if gear_limit > 2:
                        continue
                    gear_ratio = gear_ratio * int(number)
                    gear_limit = gear_limit + 1
                if line_3[element-1].isdigit():
                    # print("belowLeft")
                    number = get_number_replace_with_dot(line_3, element-1)
                    if gear_limit > 2:
                        continue
                    gear_ratio = gear_ratio * int(number)
                    gear_limit = gear_limit + 1
                if line_3[element+1].isdigit():
                    # print("belowRight")
                    number = get_number_replace_with_dot(line_3, element+1)
                    if gear_limit > 2:
                        continue
                    gear_ratio = gear_ratio * int(number)
                    gear_limit = gear_limit + 1

                if gear_limit < 3 and gear_limit > 1:
                    result = result + gear_ratio
        try:
            next_line = list(next(input_list_itterator))
        except:
            break

        line_1 = line_2
        line_2 = line_3

    return result


print(day3_part2())
