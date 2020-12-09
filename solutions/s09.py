#############
##  SETUP  ##
#############
import itertools

def setup(file):
    with open(file) as f:
        data = [int(val) for val in f.read().splitlines()]
    return data

class RollingSum:
    def __init__(self, start):
        self._values = start
        self._sums = [None] * (len(start) - 1)
        for i in range(len(start) - 1):
            self._sums[i] = [None] * len(start)
            for j in range(i + 1, len(start)):
                self._sums[i][j] = start[i] + start[j]

    def replace(self, index, value):
        index = index % len(self._values)
        delta = value - self._values[index]
        self._values[index] = value
        for i in range(len(self._values) - 1):
            if i < index:
                self._sums[i][index] = self._sums[i][index] + delta
            elif i == index:
                for j in range(i + 1, len(self._values)):
                    self._sums[i][j] = self._sums[i][j] + delta
            else:
                break
        return self

    def values(self):
        nums = set(itertools.chain.from_iterable(self._sums))
        nums.remove(None)
        return nums

preamble = 25

##############
##  PART 1  ##
##############
def part1(data):
    sums = RollingSum(data[:preamble])
    for i in range(preamble, len(data)):
        num = data[i]
        if not num in sums.values():
            return num
        sums.replace(i, num)

##############
##  PART 2  ##
##############
def part2(data):
    weak = part1(data)
    for i in range(len(data) - 1):
        sum = data[i]
        if sum >= weak:
            break
        for j in range(i + 1, len(data)):
            sum = sum + data[j]
            if sum == weak:
                return max(data[i:j + 1]) + min(data[i: j + 1])
            elif sum > weak:
                break

if __name__ == "__main__":
    data = setup("../input/09.txt")
    print("\nPart 1:")
    print(part1(data))
    print("\nPart 2:")
    print(part2(data))
