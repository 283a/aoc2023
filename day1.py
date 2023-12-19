import re


def read_input(filepath):
    numbers = list()
    with open(filepath, "r") as f:
        for line in f:
            numbers.append(line)
    return numbers


inputList = read_input("aoc2023\input1.txt")


def part1():
    """part1"""
    result = 0

    for x in inputList:
        # Iterate over each index of the string
        number1 = ""
        number2 = ""
        for i in range(len(x)):
            if x[i].isdigit():
                number1 = x[i]
                break
        for n in range(len(x) - 1, -1, -1):
            if x[n].isdigit():
                number2 = x[n]
                break
        resultnumber = number1 + number2
        result = result + int(resultnumber)

    print(result)


def part2():
    """part2"""
    result = 0
    resultnumber = "0"
    number_in_text = ["one", "two", "three", "four",
                      "five", "six", "seven", "eight", "nine"]

    for x in inputList:
        number1 = 0
        number2 = 0
        number1_index = len(x)
        number2_index = -1

        for l in range(len(number_in_text)):
            try:
                index = x.index(number_in_text[l])
            except ValueError:
                continue
            if index < number1_index:
                number1_index = index
                number1 = l+1
            index2 = x.rfind(number_in_text[l])
            if index2 > number2_index:
                number2_index = index2
                number2 = l+1
        number1 = str(number1)
        number2 = str(number2)
        for i in range(len(x)):
            if x[i].isdigit():
                if i < number1_index:
                    number1_index = i
                    number1 = x[i]
                break
        for n in range(len(x) - 1, -1, -1):
            if x[n].isdigit():
                if n > number2_index:
                    number2_index = n
                    number2 = x[n]
                    break
        resultnumber = number1 + number2
        result = result + int(resultnumber)
        print(result)

    print(result)


part2()
