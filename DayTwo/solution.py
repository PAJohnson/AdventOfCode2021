# Advent of Code Day 2
# Patrick Johnson 2021

def readInput(fname):
    # read input into [[direction, distance],...]
    data = []

    with open(fname, 'r') as f:
        for line in f:
            direction = line.split(' ')[0]
            distance = line.split(' ')[1]
            data.append((direction, int(distance)))
    return data

def part1(puzzleInput):
    position = 0
    depth = 0

    for direction, distance in puzzleInput:
        if direction == 'forward':
            position = position + distance
        elif direction == 'down':
            depth = depth + distance
        elif direction == 'up':
            depth = depth - distance
        else:
            pass

    return position * depth

def part2(puzzleInput):
    position = 0
    depth = 0
    aim = 0

    for direction, distance in puzzleInput:
        if direction == 'forward':
            position = position + distance
            depth = depth + aim * distance
        elif direction == 'down':
            aim = aim + distance
        elif direction == 'up':
            aim = aim - distance
        else:
            pass    

    return position * depth

if __name__ == "__main__":
    print(part1(readInput('input.txt')))
    print(part2(readInput('input.txt')))