# Advent Of Code Day 1
# Patrick Johnson 2021

def readInput():
    depths = []

    with open("input.txt") as inFile:
        for line in inFile:
            depths.append(int(line.strip()))

    return depths

def depthCompare(depths):
    increases = 0
    for i in range(len(depths)):
        if i == 0:
            pass
        else:
            if depths[i] > depths[i-1]:
                increases = increases + 1

    return increases 

def part1(depths):
    # read file
    # keep track of increased depths from one line to the next

    return depthCompare(depths)

def part2(depths):
    # the same, but by comparing sums of a three measurement sliding window

    newDepths = []
    for i in range(len(depths)-2):
        newDepths.append(depths[i] + depths[i+1] + depths[i+2])

    return depthCompare(newDepths)

if __name__ == "__main__":
    depths = readInput()
    print(part1(depths))
    print(part2(depths))