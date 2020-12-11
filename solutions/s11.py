#############
##  SETUP  ##
#############
def setup(file):
    with open(file) as f:
        data = f.read().splitlines()
    return Lobby(data)

class Seat:
    def __init__(self, x, y, lobby = [[]], occupied = None):
        self.x = x
        self.y = y
        self.occupied = occupied
        self.lobby = lobby

    def __add__(self, other):
        return str(self) + str(other)

    def __radd__(self, other):
        return str(other) + str(self)

    def __eq__(self, other):
        return str(self) == str(other)

    def __str__(self):
        if self.occupied == True:
            return "#"
        elif self.occupied == False:
            return "L"
        else:
            return "."

    def neighbors(self, distant = False):
        compass = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        n = 0
        if distant:
            for dx, dy in compass:
                (x0, y0) = (self.x + dx, self.y + dy)
                seat = self.lobby.get(x0, y0)
                while seat and seat.occupied == None:
                    x0 = x0 + dx
                    y0 = y0 + dy
                    seat = self.lobby.get(x0, y0)
                if seat and seat.occupied:
                    n = n + 1
        else:
            for dx, dy in compass:
                seat = self.lobby.get(self.x + dx, self.y + dy)
                if seat and seat.occupied:
                    n = n + 1
        return n

    def next_state(self, distant = False):
        if self.occupied == None:
            return "."

        tolerance = 5 if distant else 4
        neighbors = self.neighbors(distant)

        if self.occupied == False and neighbors == 0:
            return "#"
        elif self.occupied == True and neighbors >= tolerance:
            return "L"
        else:
            return str(self)

class Lobby:
    def __init__(self, data):
        self.dim_x = len(data[0])
        self.dim_y = len(data)

        self.seats = [None] * self.dim_y
        for y in range(self.dim_y):
            self.seats[y] = [None] * self.dim_x
            for x in range(self.dim_x):
                if data[y][x] == "L":
                    seat = False
                elif data[y][x] == "#":
                    seat = True
                else:
                    seat = None
                self.set(x, y, Seat(x, y, self, seat))

    def __str__(self):
        output = ""
        for y in range(self.dim_y):
            for x in range(self.dim_x):
                output = output + self.get(x, y)
            output = output + "\n"
        return output

    def __eq__(self, other):
        return str(self) == str(other)

    def __neq__(self, other):
        return str(self) != str(other)

    def get(self, x, y):
        if 0 <= x < self.dim_x and 0 <= y < self.dim_y:
            return self.seats[y][x]
        else:
            return None

    def occupied(self):
        sum = 0
        for y in range(self.dim_y):
            for x in range(self.dim_x):
                if self.get(x, y) == "#":
                    sum = sum + 1
        return sum

    def set(self, x, y, val):
        self.seats[y][x] = val
        return self

    def next_state(self, distant = False):
        state = [None] * self.dim_y
        for y in range(self.dim_y):
            row = [None] * self.dim_x
            for x in range(self.dim_x):
                row[x] = self.get(x, y).next_state(distant)
            state[y] = "".join(row)
        return Lobby(state)

##############
##  PART 1  ##
##############
def part1(data):
    state1 = data
    state2 = data.next_state()
    while state1 != state2:
        state1 = state2
        state2 = state1.next_state()
    return state1.occupied()

##############
##  PART 2  ##
##############
def part2(data):
    state1 = data
    state2 = data.next_state(True)
    while state1 != state2:
        state1 = state2
        state2 = state1.next_state(True)
    return state1.occupied()

if __name__ == "__main__":
    data = setup("../input/11.txt")
    print("\nPart 1:")
    print(part1(data))
    print("\nPart 2:")
    print(part2(data))
