from functools import reduce


def reverse_section(numbers, length, current_pos):
    indicies = [i % len(numbers) for i in range(current_pos, current_pos + length)]
    sublist = [numbers[i] for i in indicies]

    sublist.reverse()

    counter = 0
    for i in indicies:
        numbers[i] = sublist[counter]
        counter += 1


def process_list(input_lengths, upto=256, times=1):
    numbers = list(range(0, upto))
    current_pos, skip_size = 0, 0

    for _ in range(times):
        for length in input_lengths:
            reverse_section(numbers, length, current_pos)

            current_pos += (length + skip_size)
            skip_size += 1

    return numbers


def part_1(input_lengths, n=256):
    numbers = process_list(input_lengths, n)
    return numbers[0] * numbers[1]


def part_2(input_lengths):
    numbers = process_list(input_lengths, 256, 64)

    xor = lambda x, y: x ^ y
    xord = []

    for i in range(16):
        slice = numbers[i * 16:(i + 1) * 16]

        xord.append(reduce(xor, slice))

    return ''.join(map(lambda s: "%0.2X" % s, xord))


assert part_1([3, 4, 1, 5], 5) == 12

input_part1 = map(lambda s: int(s.strip()), open('./input.txt').readline().split(','))
print(part_1(input_part1))

input_part2 = [ord(c) for c in open('./input.txt').readline()] + [17, 31, 73, 47, 23]

print(part_2(input_part2))
