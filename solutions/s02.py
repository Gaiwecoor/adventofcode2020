#############
##  SETUP  ##
#############
import re

def parse(line):
    match = re.search(r"^(\d+)\-(\d+) (\w): (\w+)$", line)
    return (int(match.group(1)), int(match.group(2)), match.group(3), match.group(4))

def setup(file):
    with open(file) as f:
        data = [parse(line) for line in f.read().splitlines()]
    return data

##############
##  PART 1  ##
##############
def valid1(line):
    (min_count, max_count, character, password) = line
    count = password.count(character)
    return min_count <= count <= max_count

def part1(data):
    return sum([valid1(line) for line in data])

##############
##  PART 2  ##
##############
def valid2(line):
    (index1, index2, character, password) = line
    return (password[index1 - 1] == character) ^ (password[index2 - 1] == character)

def part2(data):
    return sum([valid2(line) for line in data])

if __name__ == "__main__":
    data = setup("../input/02.txt")
    print("\nPart 1:")
    print(part1(data))
    print("\nPart 2:")
    print(part2(data))
