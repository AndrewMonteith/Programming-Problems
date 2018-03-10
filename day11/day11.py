# Hexagonal Coordinates have been used alot in games, there are many
# articles and resources that tell you the best way to do it
# for this problem i refer to: https://www.redblobgames.com/grids/hexagons/

# The constraint used for these coordinates is: x + y + z = 0
# From this constraint u can work out how a direction affects x,y,z

def instructions(file):
    with open(file, 'r') as f:
        return f.read().split(",")


x, y, z = 0, 0, 0

def dist():
    return max(abs(x), abs(y), abs(z))

max_dist = 0
for instruction in instructions("input.txt"):
    if instruction == "ne":
        z -= 1
        x += 1
    elif instruction == "sw":
        z += 1
        x -= 1
    elif instruction == "nw":
        y += 1
        x -= 1
    elif instruction == "se":
        y -= 1
        x += 1
    elif instruction == "n":
        y += 1
        z -= 1
    elif instruction == "s":
        y -= 1
        z += 1

    cur_dist = dist()
    if cur_dist > max_dist:
        max_dist = cur_dist

print("Distance:", dist())
print("Max Distance:", max_dist)