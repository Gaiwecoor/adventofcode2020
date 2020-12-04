#############
##  SETUP  ##
#############
import re

class Passport:
    req_fields = ["byr", "iyr", "ecl", "pid", "eyr", "hcl", "hgt"]
    EXP_HGT = re.compile(r"^((59|6\d|7[0-6])in)|((1[5-8]\d|19[0-3])cm)$")
    EXP_HCL = re.compile(r"^#[0-9a-f]{6}$")
    EXP_PID = re.compile(r"^\d{9}$")

    def __init__(self, info):
        info = info.split()
        for keyVal in info:
            key_val = keyVal.split(":")
            setattr(self, key_val[0], key_val[1])

    def valid1(self):
        return [hasattr(self, field) for field in self.req_fields].count(True) == 7

    def valid2(self):
        if not self.valid1():
            return False

        for key in self.req_fields:
            value = getattr(self, key)
            if key == "byr" and not (1920 <= int(value) <= 2002):
                return False
            elif key == "iyr" and not (2010 <= int(value) <= 2020):
                return False
            elif key == "eyr" and not (2020 <= int(value) <= 2030):
                return False
            elif key == "hgt" and not self.EXP_HGT.match(value):
                return False
            elif key == "hcl" and not self.EXP_HCL.match(value):
                return False
            elif key == "ecl" and value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
            elif key == "pid" and not self.EXP_PID.match(value):
                return False

        return True

def setup(file):
    with open(file) as f:
        data = [Passport(line) for line in f.read().split("\n\n")]
    return data

##############
##  PART 1  ##
##############
def part1(data):
    return [passport.valid1() for passport in data].count(True)

##############
##  PART 2  ##
##############
def part2(data):
    return [passport.valid2() for passport in data].count(True)

if __name__ == "__main__":
    data = setup("../input/04.txt")
    print("\nPart 1:")
    print(part1(data))
    print("\nPart 2:")
    print(part2(data))
