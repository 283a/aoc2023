"""day7"""
import re
import os
import sys
from utils import read_lines_from_file

def count_chars_with_regex(input_string):
    """d"""
    char_counts = {}

    for char in set(input_string):
        occurrences = re.findall(re.escape(char), input_string)
        char_counts[char] = len(occurrences)

    return char_counts


def part1():
    """part1"""
    input_stings_list = read_lines_from_file(
        os.path.join( "input7.txt"))

    print(input_stings_list)

    pairs: list = []

    for line in input_stings_list:
        splited = line.split(maxsplit=1)
        pairs.append(splited)

    for x, pair in enumerate(pairs):
        pair.append(count_chars_with_regex(pair[0]))

    for pair in pairs:
        pair[2] = dict(sorted(pair[2].items(), key=lambda item: item[1], reverse=True))

    for pair in pairs:
        length = len(pair[2])
        if length == 1:
            print("5 of a kind")
        if length == 2:
            print("4 of a kind")
        if length == 3:
            print("4 of a kind")
    print(pairs)


part1()
