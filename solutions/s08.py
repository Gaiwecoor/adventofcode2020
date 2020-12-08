#############
##  SETUP  ##
#############
def parse_command(line):
    [c, v] = line.split()
    return (c, int(v))

def setup(file):
    with open(file) as f:
        data = [parse_command(line) for line in f.read().splitlines()]
    return data

class VM:
    def __init__(self, data):
        self.pointer = 0
        self.visited = set([0])
        self.accumulator = 0
        self.code = data
        self.complete = False

    def step(self):
        (cmd, value) = self.code[self.pointer]
        getattr(self, cmd)(value)
        self.pointer = self.pointer + 1

        if self.pointer == len(self.code):
            self.complete = True
            return False
        elif self.pointer > len(self.code) or self.pointer in self.visited:
            return False
        else:
            self.visited.add(self.pointer)
            return True

    ### OP PROCESS ###
    def acc(self, val):
        self.accumulator = self.accumulator + val

    def jmp(self, val):
        self.pointer = self.pointer + val - 1

    def nop(self, val):
        pass

##############
##  PART 1  ##
##############
def part1(data):
    vm = VM(data)
    while vm.step():
        pass
    return vm.accumulator

##############
##  PART 2  ##
##############
def part2(data):
    for i in range(len(data)):
        prog = data.copy()
        (cmd, value) = prog[i]
        if cmd == "nop":
            prog[i] = ("jmp", value)
        elif cmd == "jmp":
            prog[i] = ("nop", value)
        else:
            continue
        vm = VM(prog)
        while vm.step():
            pass
        if vm.complete:
            return vm.accumulator

if __name__ == "__main__":
    data = setup("../input/08.txt")
    print("\nPart 1:")
    print(part1(data))
    print("\nPart 2:")
    print(part2(data))
