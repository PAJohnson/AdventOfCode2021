# Advent Of Code Day 1
# Patrick Johnson 2021

def readInput():
    depths = []

    with open("input.txt") as inFile:
        for line in inFile:
            depths.append(int(line.strip()))

    return depths

def part1():
    # read file
    # keep track of increased depths from one line to the next
    depths = readInput()

    increases = 0
    for i in range(len(depths)):
        if i == 0:
            pass
        else:
            if depths[i] > depths[i-1]:
                increases = increases + 1

    return increases

def part2():
    # the same, but by comparing sums of a three measurement sliding window
    depths = readInput()

    newDepths = []
    for i in range(len(depths)-2):
        newDepths.append(depths[i] + depths[i+1] + depths[i+2])

    increases = 0
    for i in range(len(newDepths)):
        if i == 0:
            pass
        else:
            if newDepths[i] > newDepths[i-1]:
                increases = increases + 1

    return increases    

if __name__ == "__main__":
    print(part1())
    print(part2())