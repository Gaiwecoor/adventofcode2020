#############
##  SETUP  ##
#############
def setup(file):
    with open(file) as f:
        data = f.read().splitlines()
    return data

##############
##  PART 1  ##
##############
def part1(data):
    pass

##############
##  PART 2  ##
##############
def part2(data, p1):
    pass

if __name__ == "__main__":
    data = setup("../input/input.txt")
    print("\nPart 1:")
    p1 = part1(data)
    print(p1)
    print("\nPart 2:")
    print(part2(data, p1))
