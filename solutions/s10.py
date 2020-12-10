#############
##  SETUP  ##
#############
def setup(file):
    with open(file) as f:
        data = [int(l) for l in f.read().splitlines()]
    data.append(0)
    data.append(max(data) + 3)
    data.sort()
    return data

##############
##  PART 1  ##
##############
def part1(data):
    diffs = [0] * 4
    jolt = 0
    for adapter in data:
        diffs[adapter - jolt] = diffs[adapter - jolt] + 1
        jolt = adapter
    return diffs[1] * diffs[3]

##############
##  PART 2  ##
##############
def part2(data):
    paths = [0] * len(data)
    paths[0] = 1
    for adapter in range(1, len(data)):
        for prev in range(max(0, adapter - 3), adapter):
            if data[adapter] - data[prev] <= 3:
                paths[adapter] = paths[adapter] + paths[prev]
    return paths[len(paths) - 1]

if __name__ == "__main__":
    data = setup("../input/10.txt")
    print("\nPart 1:")
    print(part1(data))
    print("\nPart 2:")
    print(part2(data))
