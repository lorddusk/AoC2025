from utils.read import read_file

def part_one(_input):
    pos = 50
    password = 0
    for rotation in _input:
        direction = rotation[:1]
        amount = rotation[1:]

        amt = int(amount)
        if direction == "L":
            for i in range(amt):
                pos -= 1
                if pos == -1:
                    pos = 99
            if pos == 0:
                password += 1

        if direction == "R":
            for i in range(amt):
                pos += 1
                if pos == 100:
                    pos = 0
            if pos == 0:
                password += 1

    print(f"Part 1 - The actual password to open the door is: {password}")


def part_two(_input):
    pos = 50
    password = 0
    for rotation in _input:
        direction = rotation[:1]
        amount = rotation[1:]

        amt = int(amount)
        if direction == "L":
            for i in range(amt):
                pos -= 1
                if pos == -1:
                    pos = 99
                if pos == 0:
                    password += 1

        if direction == "R":
            for i in range(amt):
                pos += 1
                if pos == 100:
                    pos = 0
                if pos == 0:
                    password += 1

    print(f"Part 2 - The actual password to open the door is: {password}")


if __name__ == "__main__":
    stringInput = read_file(1, "string", False)
    part_one(stringInput)
    part_two(stringInput)
