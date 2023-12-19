"""day5"""
import re
import os
from utils import read_lines_from_file

def day5_part1():
    """part1"""
    input_list = read_lines_from_file(os.path.join("input5.txt"))

    seed_list = re.findall(r'\d+', input_list[0])
    seed_list = [int(num) for num in seed_list]

    number_list = []
    for i, input_string in enumerate(input_list):
        if i < 2:
            continue
        numbers = re.findall(r'\d+', input_string)
        numbers = [int(num) for num in numbers]

        number_list.append(numbers)

    for n in range(seed_list):
        map_finished = False
        for numbers in number_list:
            if len(numbers) == 0:
                map_finished = False
            if len(numbers) > 0 and seed_list[n] >= numbers[1] and seed_list[n]< (numbers[1]+numbers[2]) and not map_finished:
                seed_list[n] = numbers[0]+(seed_list[n]-numbers[1])
                map_finished = True

    return min(seed_list)

def day5_part2():
    """part2"""
    input_list = read_lines_from_file(os.path.join("input5.txt"))

    seed_list = re.findall(r'\d+', input_list[0])
    seed_list = [int(num) for num in seed_list]

    number_list = []
    for i, input_string in enumerate(input_list):
        if i < 2:
            continue
        numbers = re.findall(r'\d+', input_string)
        numbers = [int(num) for num in numbers]

        number_list.append(numbers)

    result = []
    l = 0
    for n in range(0,len(seed_list),2):
        for x in range(seed_list[n],seed_list[n]+seed_list[n+1]):
            map_finished = False
            for numbers in number_list:
                if len(numbers) == 0:
                    map_finished = False
                if len(numbers) > 0 and x >= numbers[1] and x< (numbers[1]+numbers[2]) and not map_finished:
                    x = numbers[0] +(x-numbers[1])
                    map_finished = True
            result.append(x)

    print(min(result))

print(day5_part2())
