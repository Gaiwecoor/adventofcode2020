#############
##  SETUP  ##
#############
bags = None

class Bag:
    def __init__(self, container, contents):
        self.color = container
        self.has = {}

        self.shiny_gold = None
        self.bag_count = 0

        for bag in contents:
            (q, c) = bag.split(" ", 1)
            self.has[c] = int(q)

    def has_gold(self):
        if not self.shiny_gold == None:
            return self.shiny_gold
        elif self.has.get("shiny gold"):
            self.shiny_gold = True
            return True
        else:
            for key in self.has:
                bag = bags.get(key)
                if bag.has_gold():
                    self.shiny_gold = True
                    return True
            self.shiny_gold = False
            return False

    def weight(self):
        if not self.bag_count == 0:
            return self.bag_count
        else:
            weight = 1
            for key, quantity in self.has.items():
                bag = bags.get(key)
                weight = weight + (quantity * bag.weight())
            self.bag_count = weight
            return weight

def setup(file):
    global bags
    rules = {}

    def parse(line):
        (container, contains) = line.split("  contain ")
        contents = contains.strip().split(" , ")
        if contents[0] == "":
            contents = []
        return Bag(container, contents)

    with open(file) as f:
        data = f.read()
        trim = ["no other bags", "bags", "bag", "."]
        for str in trim:
            data = data.replace(str, "")
        for line in data.splitlines():
            bag = parse(line)
            rules[bag.color] = bag

    bags = rules
    return rules

##############
##  PART 1  ##
##############
def part1(data):
    count = 0
    for bag in data.values():
        if bag.has_gold():
            count = count + 1
    return count

##############
##  PART 2  ##
##############
def part2(data):
    return data.get("shiny gold").weight() - 1

if __name__ == "__main__":
    data = setup("../input/07.txt")
    print("\nPart 1:")
    print(part1(data))
    print("\nPart 2:")
    print(part2(data))
