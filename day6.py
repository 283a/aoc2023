"""day6"""
import re

def read_input(filepath):
    numbers = list()
    with open(filepath, "r") as f:
        for line in f:
            numbers.append(line)
    return numbers

def day6_part1():
    """part1"""
    input_list = read_input("aoc2023\input6.txt")

    times = re.findall(r'\d+', input_list[0])
    distances = re.findall(r'\d+', input_list[1])

    result = 1

    for x in range(0,len(times)):

        time_given = int(times[x])

        count = 0

        for time_pressed in range(1,time_given):
            distance_raced = (time_given - time_pressed) * time_pressed
            if(distance_raced > int(distances[x])):
                count = count + 1

        result = result * count        

    return result


def day6_part2():
    """part2"""
    input_list = read_input("aoc2023\input6.txt")

    times = re.findall(r'\d+', input_list[0])
    distances = re.findall(r'\d+', input_list[1])

    time = ""
    distance = ""

    for x in times:
        time = time + x
    for n in distances:
        distance = distance + n

    time_given = int(time)

    count = 0

    for time_pressed in range(1,time_given):
        distance_raced = (time_given - time_pressed) * time_pressed
        if distance_raced > int(distance):
            count = count + 1

    return count

print(day6_part2())
