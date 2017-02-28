import argparse
import csv

import random

parser = argparse.ArgumentParser('names.py',
                                 description='A really, really, really, really, really stupid random name generator')
parser.add_argument('-f', '--csv-file', help='CSV file to pull names from', default='names.csv')
parser.add_argument('-n', '--number', help='number of names to generate', default=10)
parser.add_argument('-r', '--randomize', help='create random names', action='store_true')
parser.add_argument('-c', '--column-names', help='column names from csv file',
                    default='first_name,middle_name,last_name')


def main_from_cli(argv):
    args = parser.parse_args(argv)
    return main_from_args(args)


def main_from_args(args):
    main(args.csv_file, args.number, args.randomize, args.column_names)


def generate_random(items, name_parts):
    return build_name(*[items[random.randint(-1, len(items) - 1)].get(name_parts[i]) for i in range(len(name_parts))])


def build_name(*args):
    return ' '.join(args).replace('  ', ' ').strip()


def get_names(reader):
    return list(reader)


def main(csv_file='names.csv', number=1000, randomize=True, column_names='first_name,middle_name,last_name'):
    name_parts = column_names.split(',')
    with open(csv_file) as f:
        names = get_names(csv.DictReader(f))
        number = min(number, len(names))
        while number > 0:
            if randomize:
                print(generate_random(names, name_parts))

            else:
                row = names[random.randint(-1, len(names) - 1)]
                print(build_name(*[row.get(name_parts[i]) for i in range(len(name_parts))]))
            number -= 1


if __name__ == '__main__':
    import sys

    main_from_cli(sys.argv[1:])
