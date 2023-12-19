"""day4"""
import os
import re
from utils import read_lines_from_file

def day4_part1():
    """part1"""
    input_list = read_lines_from_file(os.path.join("aoc2023", "input4.txt"))
    result = 0

    for line in input_list:

        slash_index = line.find('|')
        point_index = line.find(':')

        winner = re.findall(r'\d+', line[point_index:slash_index])

        given = re.findall(r'\d+', line[slash_index:])

        line_count = 0

        for val in winner:
            if val in given:
                if line_count == 0:
                    line_count = 1
                else:
                    line_count = line_count * 2
        result += line_count

    return result

def day4_part2():
    """part2"""
    input_list = read_lines_from_file(os.path.join("aoc2023", "input4.txt"))

    slash_index = input_list[0].find('|')
    point_index = input_list[0].find(':')

    counter = []

    for x in range(0,len(input_list)):
        counter.append(1)

    for x in range(0,len(input_list)):

        winner = re.findall(r'\d+', input_list[x][point_index:slash_index])
        
        given = re.findall(r'\d+', input_list[x][slash_index:])

        line_count = 0

        for val in winner:
            if val in given:
                line_count += 1
        
        for n in range(1,line_count+1):
            counter[x+n] += 1 * counter[x]

    return sum(counter)

# print(day4_part1())
print(day4_part2())
