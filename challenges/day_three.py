f = open("/Users/caitlinhamilton/Programming/advent_of_code_2020/input_data/day_three.txt", "r")
data = f.read().splitlines()
data.pop(0)


def part_one(x_index, data):
    jump = x_index
    width_of_row = len(data[0])
    tree_count = 0
    for row in data:
        if x_index >= width_of_row:
            x_index = x_index % width_of_row
        if row[x_index] == '#':
            tree_count += 1
        x_index += jump
    return tree_count


def part_two(x_index, data):
    del data[::2]
    return part_one(x_index, data)

ans1 = part_one(1, data)
ans2 = part_one(3, data)
ans3 = part_one(5, data)
ans4 = part_one(7, data)

ans5 = part_two(1, data)

print(ans1 * ans2 * ans3 * ans4 * ans5)


#3510149120