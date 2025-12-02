from utils.read import read_file


def part_one(_input):
    invalid_ids = []
    for _range in _input:
        start, end = _range.split('-')
        for _id in range(int(start), int(end) + 1):
            num = str(_id)
            numLength = int(len(num) / 2)
            firstHalf = num[:numLength]
            secondHalf = num[numLength:]
            if firstHalf == secondHalf:
                invalid_ids.append(_id)
    print(f"Part 1 - Sum of invalid IDs: {sum(invalid_ids)}")


def part_two(_input):
    invalid_ids = []
    for _range in _input:
        start, end = _range.split('-')
        for _id in range(int(start), int(end) + 1):
            id_str = str(_id)
            n = len(id_str)
            for sub_len in range(1, n // 2 + 1):
                if n % sub_len == 0:
                    sub_num = id_str[:sub_len]
                    if sub_num * (n // sub_len) == id_str:
                        invalid_ids.append(_id)
                        break
    print(f"Part 2 - Sum of invalid IDs: {sum(invalid_ids)}")


if __name__ == "__main__":
    stringInput = read_file(2, "string", False)
    rangeInput = stringInput[0].split(',')
    part_one(rangeInput)
    part_two(rangeInput)
