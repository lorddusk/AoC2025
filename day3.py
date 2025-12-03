from utils.read import read_file

def part_one(_input):
    joltage = []
    for bank in _input:
        max_joltage = 0
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                current_joltage = int(f"{bank[i]}{bank[j]}")
                max_joltage = max(max_joltage, current_joltage)
        joltage.append(max_joltage)
    print(f"Part 1 - Total output Joltage: {sum(joltage)}")


def part_two(_input):
    batteries = 12
    joltage = []
    for bank in _input:
        last_position = 0
        bank_number = ''

        for battery in range(batteries):
            max_digit = '0'
            for position in range(last_position, len(bank) - batteries + battery + 1):
                if int(bank[position]) > int(max_digit):
                    max_digit = bank[position]
                    last_position = position
            last_position += 1
            bank_number += max_digit
        joltage.append(int(bank_number))
    print(f"Part 2 - Total output Joltage: {sum(joltage)}")


if __name__ == "__main__":
    stringInput = read_file(3, "string", False)
    part_one(stringInput)
    part_two(stringInput)
