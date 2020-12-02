def setup(input):
    with open(input) as f:
        data = [int(line) for line in f.read().splitlines()]
    return data

def part1(data):
    data.sort()
    for num1 in range(len(data) - 1):
        for num2 in range(num1 + 1, len(data)):
            sum = data[num1] + data[num2]
            if sum > 2020:
                break
            elif sum == 2020:
                return (data[num1] * data[num2])

def part2(data):
    for num1 in range(len(data) - 2):
        for num2 in range(num1 + 1, len(data) - 1):
            sumA = data[num1] + data[num2]
            if (sumA > 2020): break
            for num3 in range(num2 + 1, len(data)):
                sum = sumA + data[num3]
                if sum > 2020: break
                elif sum == 2020:
                    return (data[num1] * data[num2] * data[num3])

if __name__ == "__main__":
    data = setup("../input/01.txt")
    print("\nPart 1:")
    print(part1(data))
    print("\nPart 2:")
    print(part2(data))
