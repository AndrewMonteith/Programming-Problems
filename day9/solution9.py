def calculate_score(text):
    ctr_ptr, depth, score, total_garbage = 0, 0, 0, 0

    def can_read():
        return ctr_ptr < len(text)

    def read_letter():
        nonlocal ctr_ptr

        letter = text[ctr_ptr]
        if letter == "!":
            ctr_ptr += 2
            if not can_read():
                return None
            return read_letter()

        ctr_ptr += 1

        return letter

    is_garbage = False

    while can_read():
        letter = read_letter()

        if is_garbage and letter != ">":
            total_garbage += 1
        elif letter == "<":
            is_garbage = True
        elif letter == ">":
            is_garbage = False
        elif not is_garbage:
            if letter == "{":
                depth += 1
            elif letter == "}":
                score += depth
                depth -= 1

    return score, total_garbage


assert calculate_score("{}") == (1, 0)
assert calculate_score("{{{}}}") == (6, 0)
assert calculate_score("{{}, {}}") == (5, 0)
assert calculate_score("{{{},{},{{}}}}") == (16, 0)
assert calculate_score("{<a>,<a>,<a>,<a>,<a>}") == (1, 5)
assert calculate_score("{{<ab>},{<ab>},{<ab>},{<ab>}}") == (9, 8)
assert calculate_score("{{<!!>},{<!!>},{<!!>},{<!!>}}") == (9, 0)
assert calculate_score("{{<a!>},{<a!>},{<a!>},{<ab>}}") == (3, 17)

print(calculate_score(open('./input.txt').readline()))
