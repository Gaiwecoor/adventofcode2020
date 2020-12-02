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
def part2(data):
    pass

if __name__ == "__main__":
    data = setup("../input/input.txt")
    print("\nPart 1:")
    print(part1(data))
    print("\nPart 2:")
    print(part2(data))
