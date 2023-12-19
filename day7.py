"""day7"""
import re
import os
from utils import read_lines_from_file

def is_five_of_a_kind(input_string):
    """are_all_chars_equal"""
    return bool(re.match(r'^(\S)\1*$', input_string))

def is_four_of_a_kind(input_string):
    """has_four_equal_chars"""
    return bool(re.search(r'(.)\1{3}', input_string))

def full_house(input_string):
    """has_specific_hand_pattern"""
    match = re.match(r'^([AKQJT98765432])\1{2}([AKQJT98765432])\2$', input_string)
    return bool(match)

def is_three_of_a_kind_hand(input_string):
    """has_specific_hand_pattern"""
    match = re.match(r'^([AKQJT98765432])\1{2}(?:(?!\1)[AKQJT98765432](?:(?!\1)[AKQJT98765432](?:(?!\1)[AKQJT98765432])?)?)?$', input_string)
    return bool(match)

def two_pair(input_string):
    """has_specific_hand_pattern"""
    match = re.match(r'^([AKQJT98765432])\1([AKQJT98765432])\2(?:([AKQJT98765432])\3)?$', input_string)
    return bool(match)


def part1():
    """part1"""
    input_stings_list = read_lines_from_file(os.path.join("aoc2023","input7.txt"))

    print(input_stings_list)

    pairs : list = []

    for line in input_stings_list:
        splited = line.split(maxsplit=1)
        pairs.append(splited)

    for x,pair in enumerate(pairs):
        if is_four_of_a_kind(pair[0]):
            print("okok")
    print(pairs)
part1()