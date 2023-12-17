import re
import os

def read_input(filepath):
    numbers = list()
    with open(filepath, "r") as f:
        numbers = f.readlines()
    return numbers

def day2_part1():
    input_list = read_input(os.path.join("aoc2023", "input2.txt"))
    result = 0

    for input_str in input_list:
        input_str = input_str.strip()

        match = re.search(r':\s*(.+)', input_str)

        if match:
            game_data_string = match.group(1)

            matches = re.findall(r'(\d+)\s*([\w\s]+)', game_data_string)

            possible = all(int(number) <= 12 or (color == 'red' and int(number) <= 12) or
                           (color == 'green' and int(number) <= 13) or
                           (color == 'blue' and int(number) <= 14) for number, color in matches)

            if possible:
                number_before_colon = re.search(r'(\d+):', input_str)
                result += int(number_before_colon.group(1))

    return result

def day2_part2():
    input_list = read_input(os.path.join("aoc2023", "input2.txt"))
    result = 0

    for input_str in input_list:
        input_str = input_str.strip()

        match = re.search(r':\s*(.+)', input_str)

        red_smallest = 1
        green_smallest = 1
        blue_smallest = 1

        if match:
            game_data_string = match.group(1)

            matches = re.findall(r'(\d+)\s*([\w\s]+)', game_data_string)

            for number, color in matches:
                number = int(number)

                if color == 'red' and red_smallest < number: 
                    red_smallest = number
                if color == 'green' and green_smallest < number: 
                    green_smallest = number
                if color == 'blue' and blue_smallest < number: 
                    blue_smallest = number

            result += (red_smallest*green_smallest*blue_smallest)

    return result

# print(day2_part1())
print(day2_part2())