#!/usr/local/sbin/python
import sys
from collections import Counter


def get_file(filename):
    with open(filename, 'r') as fh:
        file_data = fh.read()
        fh.close()
        return file_data

def create_dic(data):
    num_dic = Counter()
    for item in data.split():
        num_dic[item] = len(item)
    return num_dic


def main():
    """
    Main Function calls other fuctions
    """
    file_data = get_file(sys.argv[1])
    num_dic = create_dic(file_data)
    print(num_dic.most_common())


if __name__ == '__main__':
    main()
