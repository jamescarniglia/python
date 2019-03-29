#!/usr/local/bin/python
#
"""Reads in stdin or file(s) and finds the 100 most common 3 word phrases"""
#
__version__ = "0.0.2"
#
#
import sys
import string
import re
import argparse
from collections import deque, Counter
from tabulate import tabulate


def read_in_file(flat_files, stream):
    """
    Reads in file(s) or input stream
    Sends data to clean_data

    Returns scrubbed data from input
    """
    if flat_files:
        files_blob = " "
        # may have mulitple files read in all to blob
        for each_file in flat_files:
            each_file = open(each_file, 'r')
            files_blob += each_file.read()
            each_file.close()
        # Send blob to clean_data to be cleaned
        list_data = clean_data(files_blob)
        return list_data
    elif stream:
        # If stdin then read in data and send to clean_data
        str_input = ' '.join(sys.stdin.readlines())
        list_data = clean_data(str_input)
        return list_data


def clean_data(info):
    """
    Reads in string
    Strips punctuation
    Strips new lines, tabs
    Forces all text to lowercase

    Returns scrubbed data as a deque list
    """
    clean_info_nopo = info.translate(None, string.punctuation)
    clean_info_lower = clean_info_nopo.lower()
    cleaned = re.sub(r"\s+", " ", clean_info_lower)
    # setup as deque collection for speed
    cleaned = deque(cleaned.split())
    return cleaned


def pop_through_data(data):
    """
    Reads in list
    Generates another list of phrases with 3 words

    returns the 100 most common 3 word phrases
    """
    # Setup deque list for speed
    phrases = deque('')
    # Setup counter to iterate over words
    # shouldn't iterate over list bc it is being manipluated
    count = len(data)
    while count > 3:
        # Append 3 word phrases into list
        phrases.append(data[0] + " " + data[1] + " " + data[2])
        count = count - 1
        # remove first item in the list
        data.popleft()
    # find the 100 most common strings
    common = Counter(phrases).most_common(100)
    return common


def sorter_printer(found_entries):
    """
    Input list
    Turns list into dic

    returns sorted list as table
    """
    # make list a dic so we can grab the value for sorting
    dict_common = dict(found_entries)
    # Sort by value
    ordered_common = sorted(dict_common.items(), reverse=True, key=lambda t: t[1])
    # put the list in a table for easy reading
    table = tabulate(ordered_common, headers=['Phrase', 'Occurances'])

    return table


def parser():
    """
    Argparse require stdin or files flag
    """
    arg_parser = argparse.ArgumentParser()
    group = arg_parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-files', nargs='*', help='File(s) to read in')
    group.add_argument('-stdin', action='store_true', default=False)
    args = arg_parser.parse_args()

    return args.files, args.stdin


def main():
    """
    Main Function calls other fuctions
    """
    # send to arg checker
    files, read_in = parser()
    # open either stdin or files
    list_data = read_in_file(files, read_in)
    # grab the list of phrases and the number of occurances
    common = pop_through_data(list_data)
    # sort them and place them into a table
    table = sorter_printer(common)
    # print the table to the user
    print(table)

    # return used for unit test
    return table


if __name__ == '__main__':
    main()
