# This solution was ported from C# code when I decided i wanted to get more comfortable with python
# since this solution was already correct I decided not to port the associated unit tests.

import re


def process_checksum(input_file, row_action):
    result = 0

    with open(input_file) as reader:
        for line in reader.readlines():
            numbers = [int(num) for num in filter(None, re.split('\W+', line))]  # split&cast numbers by whitespace
            result += row_action(numbers)

    return result


def parse_checksum_part1(input_file):
    return process_checksum(input_file, lambda row: max(row) - min(row))


def parse_checksum_part2(input_file):
    def pairs(row):  # reliably informed itertools.combinations is what i want.
        for a in range(0, len(row) - 1):
            for b in range(a + 1, len(row)):
                yield max(row[a], row[b]), min(row[a], row[b])

    def shared_factor(row):
        for max_num, min_num in pairs(row):
            if max_num % min_num == 0:
                return max_num / min_num
        return 0

    return process_checksum(input_file, shared_factor)


print(parse_checksum_part1("./data.txt"))
print(parse_checksum_part2("./data.txt"))
