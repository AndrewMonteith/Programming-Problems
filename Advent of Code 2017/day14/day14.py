import knothash

INPUT_STRING = "ugkiagan"

def to_bin_string(hex):
    scale = 16  ## equals to hexadecimal

    num_of_bits = 128

    return bin(int(hex, scale))[2:].zfill(num_of_bits)

total_used_squares = 0

hash_table = []

for i in range(128):
    hash_string_for_row = ('%s-%d') % (INPUT_STRING, i)

    h = knothash.hash(hash_string_for_row)

    binary_expansion = to_bin_string(h)

    hash_table.append(list(binary_expansion))

    total_used_squares += binary_expansion.count('1')

# Now we need to count the groups
total_groups = 0

def get(i, j):
    return hash_table[j][i]

def in_range(i, j):
    return 0 <= i < 128 and 0 <= j < 128

def remove(i, j):
    hash_table[j][i] = '0'

def remove_group(i, j):
    ones = [(i, j)]
    while len(ones) > 0:
        (i, j) = ones.pop()
        remove(i, j)
        for ni, nj in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]: # check neighbours
            if in_range(ni, nj) and get(ni, nj) == '1':
                    ones.append((ni, nj))


for i in range(128):
    for j in range(128):
        if get(i, j) == '1':
            total_groups += 1
            remove_group(i, j)


print("Total Squares Used:", total_used_squares)
print("Total Groups:", total_groups)