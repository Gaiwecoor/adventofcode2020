#############
##  SETUP  ##
#############
def setup(file):
    with open(file) as f:
        data = [int(seat, 2) for seat in f.read().replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1").splitlines()]
    data.sort()
    return data

##############
##  PART 1  ##
##############
def part1(data):
    return data[len(data) - 1]

##############
##  PART 2  ##
##############
def part2(data):
    first = data[0]
    last = data[len(data) - 1]
    for seat in range(first, last + 1):
        if seat not in data:
            return seat

if __name__ == "__main__":
    data = setup("../input/05.txt")
    print("\nPart 1:")
    print(part1(data))
    print("\nPart 2:")
    print(part2(data))
