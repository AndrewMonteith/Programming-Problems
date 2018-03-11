def valid_phrase(phrase: str):
    words = phrase.split(' ')

    for word in words:
        s = sorted(word)
        if words.count(word) > 1 or any(w != word and sorted(w) == s for w in words):
            return False
    return True


assert valid_phrase("aa bb cc dd")
assert not valid_phrase("aa bb cc dd aa")
assert valid_phrase("aa bb cc dd aaa")


def count_all_matching(file_name):
    with open(file_name, 'r') as file:
        s = 0

        for line in file.readlines():
            if valid_phrase(line.strip()):
                s += 1

        return s


print(count_all_matching('./input'))
