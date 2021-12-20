# Advent of Code Day 6
# Patrick Johnson 2021

# Lanternfish
# each fish has a timer
# each day, timer counts down. At 0, self timer resets to 6 + new fish produced with timer of 8
# What data structure to use?

def makeDict():
    data = {
        0 : 0,
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
        7 : 0,
        8 : 0
    }
    return data

def readInput(fname):
    data = makeDict()
    with open(fname) as f:
        fstr = f.read().strip().split(',')
        for day in fstr:
            data[int(day)] += 1

    return data

def step(data):
    # want to "rotate" each member of data down 1
    newData = makeDict()
    newData[8] += data[0]
    newData[7] += data[8]
    newData[6] += data[7]
    newData[6] += data[0]
    newData[5] += data[6]
    newData[4] += data[5]
    newData[3] += data[4]
    newData[2] += data[3]
    newData[1] += data[2]
    newData[0] += data[1]
    return newData

def total(data):
    return sum(data.values())

# simulate for 80 days
def part1(data):
    for i in range(80):
        data = step(data)
    
    return total(data)

# simulate for 256 days
def part2(data):
    for i in range(256):
        data = step(data)
    
    return total(data)

def readInputSlow(fname):
    fishes = []
    with open(fname) as f:
        fishes = [int(fish) for fish in f.read().strip().split(',')]

    return fishes

def stepSlow(fishes):
    newFishes = []
    for fish in fishes:
        if fish == 0:
            newFishes.append(6)
            newFishes.append(8)
        else:
            newFishes.append(fish-1)
    
    return newFishes

def part1Slow(data):
    for i in range(80):
        print(f'Part 1 Day {i}')
        data = stepSlow(data)

    return len(data)

def part2Slow(data):
    for i in range(256):
        print(f'Part 2 Day {i}')
        data = stepSlow(data)

    return len(data)

if __name__ == "__main__":
    fname = 'sample.txt'
    #fname = 'input.txt'

    data = readInput(fname)

    solution_1 = part1(data)
    print(solution_1)

    solution_2 = part2(data)
    print(solution_2)

    # for fun, make a slow version
    data = readInputSlow(fname)

    solution_1 = part1Slow(data)
    print(solution_1)

    solution_2 = part2Slow(data)
    print(solution_2)