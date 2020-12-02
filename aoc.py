import sys
day = sys.argv[1]

aoc = getattr(__import__("solutions.s" + day), "s" + day)

#################
##  EXECUTION  ##
#################
data = aoc.setup("./input/" + day + ".txt")

print("\nPart 1:")
print(aoc.part1(data))

print("\nPart 2:")
print(aoc.part2(data))
