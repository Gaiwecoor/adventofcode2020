#############
##  SETUP  ##
#############
import math

def setup(file):
    with open(file) as f:
        data = f.read().splitlines()
    return data

def get_pos(field, pt):
    lat = field[pt[1]]
    return lat[pt[0] % len(lat)] == "#"

##############
##  PART 1  ##
##############
def part1(field, delta = (3, 1)):
    pos = delta
    trees = 0

    while pos[1] < len(field):
        if get_pos(field, pos):
            trees = trees + 1
        pos = (pos[0] + delta[0], pos[1] + delta[1])
    return trees

##############
##  PART 2  ##
##############
def part2(field):
    deltas = [ (1, 1), (3, 1), (5, 1), (7, 1), (1, 2) ]
    trees = []
    for delta in deltas:
        trees.append(part1(field, delta))
    return math.prod(trees)

if __name__ == "__main__":
    data = setup("../input/03.txt")
    print("\nPart 1:")
    print(part1(data))
    print("\nPart 2:")
    print(part2(data))
