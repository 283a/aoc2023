"""day8 Automaten!"""
import re
import os
from utils import read_lines_from_file


def part1():
    """part1"""
    input_stings = read_lines_from_file(
        os.path.join("input8.txt"))

    letter_sequences = {}

    for x, input_string in enumerate(input_stings):
        if x < 1:
            continue
        letter_sequence: str = re.findall(r'[A-Z]+', input_string)
        letter_sequences[letter_sequence[0]] = [
            letter_sequence[1], letter_sequence[2]]

    count = 0
    key = 'AAA'
    while key != 'ZZZ':
        for inputi in input_stings[0]:
            if inputi == 'R':
                key = letter_sequences[key][1]
                print("r", key)
            else:
                key = letter_sequences[key][0]
                print("l", key)
            count += 1
            if key == 'ZZZ':
                break

    print(count)


def part2():
    """part2"""
    input_stings = read_lines_from_file(
        os.path.join("input8.txt"))

    letter_sequences = {}
    keys = []

    for x, input_string in enumerate(input_stings):
        if x < 1:
            continue
        letter_sequence: str = re.findall(r'[A-Z0-9]+', input_string)
        if 'A' in letter_sequence[0]:
            keys.append(letter_sequence[0])
        letter_sequences[letter_sequence[0]] = [
            letter_sequence[1], letter_sequence[2]]

    finished = False
    finished = all('Z' in s for s in keys)

    count  = 0
    while not finished:
        for inputi in input_stings[0]:
            for x,key in enumerate(keys):
                if inputi == 'R':
                    keys[x] = letter_sequences[key][1]
                else:
                    keys[x] = letter_sequences[key][0]
            count += 1
            finished = all('Z' in s for s in keys)
            if finished:
                break
            print(count)

    print(count)


part2()
