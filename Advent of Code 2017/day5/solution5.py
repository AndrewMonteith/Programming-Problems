def go_until_exit(instructions, is_part_2=False):
    ctr_ptr = 0

    num_of_jumps = 0

    def increment(instruction):
        if not is_part_2:
            return 1
        else:
            return -1 if instruction >= 3 else 1

    while ctr_ptr < len(instructions):
        delta_pos = instructions[ctr_ptr]
        old_ptr = ctr_ptr

        ctr_ptr += delta_pos
        delta_pos += increment(delta_pos)

        instructions[old_ptr] = delta_pos
        num_of_jumps += 1

    return num_of_jumps


def execute_maze_from_file(input_file, is_part_2=False):
    with open(input_file) as file:
        return go_until_exit(list(
            map(int, file.readlines())), is_part_2)


assert go_until_exit([0, 3, 0, 1, -3]) == 5
assert go_until_exit([0, 3, 0, 1, -3], True) == 10

print(execute_maze_from_file("./input", True))
