#############
##  SETUP  ##
#############
def setup(file):
    with open(file) as f:
        data = f.read().split("\n\n")
    return data

##############
##  PART 1  ##
##############
def part1(data):
    sum = 0
    for group in data:
        dec = set()
        answers = group.split()
        for answer in answers:
            dec.update(list(answer))
        sum = sum + len(dec)
    return sum

##############
##  PART 2  ##
##############
def part2(data):
    sum = 0
    for group in data:
        answers = group.split()
        dec = set(answers[0])
        for i in range(1, len(answers)):
            dec.intersection_update(list(answers[i]))
        sum = sum + len(dec)
    return sum

if __name__ == "__main__":
    data = setup("../input/06.txt")
    print("\nPart 1:")
    print(part1(data))
    print("\nPart 2:")
    print(part2(data))
