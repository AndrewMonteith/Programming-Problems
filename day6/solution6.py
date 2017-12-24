def process_new_state(state, start_index):
    max_val = state[start_index]
    state[start_index] = 0

    while max_val > 0:
        start_index += 1
        state[start_index % len(state)] += 1
        max_val -= 1


def next_state(previous_state):
    max_value = max(previous_state)
    all_max_blocks = [i for i, x in enumerate(previous_state) if x == max_value]

    move_index = all_max_blocks[0] if len(all_max_blocks) == 1 else min(all_max_blocks)

    process_new_state(previous_state, move_index)


def count_steps(inital_state):
    previous_states = [inital_state[:]]

    number_of_steps = 0
    current_state = inital_state

    while True:
        number_of_steps += 1
        next_state(current_state)

        if current_state in previous_states:
            return number_of_steps
        else:
            previous_states.append(current_state[:])  # need to remember to copy list.


assert count_steps([0, 2, 7, 0]) == 5
assert count_steps([4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]) == 12841


def count_steps_part2(inital_state):
    previous_states = [[inital_state[:], 0]]
    number_of_steps = 0
    current_state = inital_state

    while True:
        number_of_steps += 1
        next_state(current_state)

        matching_element = list(filter(lambda l: l[0] == current_state, previous_states))

        if any(matching_element):
            return number_of_steps - matching_element[0][1]
        else:
            previous_states.append([current_state[:], number_of_steps])


assert count_steps_part2([0, 2, 7, 0]) == 4
print(count_steps_part2([4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]))
