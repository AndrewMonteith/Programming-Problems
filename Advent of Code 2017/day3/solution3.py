# We define 1 as (0, 0) meaning a spiral walk is
# (0, 0) -> (1, 0) -> (1, 1), (0, 1) -> (-1, 1) -> (-1, 0) -> ...

DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]


def spiral_walk():
    # Coordinates of current square.
    current_x, current_y = 0, 0

    # d_index points to the required change of the direction from DX and DY
    # d_ifreq represents the amount of times we take that change of direction: 1, 1, 2, 2, 3, 3, ...
    d_index, d_ifreq = 0, 1

    spiral_n = 1  # Spiral Number.

    while True:
        for _ in range(0, 2):
            for _ in range(0, d_ifreq):
                yield (current_x, current_y), spiral_n

                current_x += DX[d_index % 4]
                current_y += DY[d_index % 4]

                spiral_n += 1
            d_index += 1
        d_ifreq += 1


def manhattan_distance(number):
    for coord, spiral_number in spiral_walk():
        if spiral_number == number:
            return abs(coord[0]) + abs(coord[1])


def first_number_above(above):
    new_spiral = {(0, 0): 1}

    def value_for(coordinate):
        # Cumulative sum of all values around coordinate.
        cx, cy = coordinate

        new_value = 0

        for x in range(cx - 1, (cx + 1) + 1):
            for y in range(cy - 1, (cy + 1) + 1):
                spiral_coord = (x, y)

                if spiral_coord != coordinate:
                    new_value += new_spiral.get(spiral_coord, 0)

        return new_value

    for coord, _ in spiral_walk():
        if coord not in new_spiral:
            value = value_for(coord)

            if value > above:
                print(value)
                break
            else:
                new_spiral[coord] = value


assert manhattan_distance(1) == 0
assert manhattan_distance(12) == 3
assert manhattan_distance(23) == 2
assert manhattan_distance(1024) == 31
assert manhattan_distance(347991) == 480
print(first_number_above(347991))
