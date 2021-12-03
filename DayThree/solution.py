# Advent of Code Day 3
# Patrick Johnson

def readInput(fname):
    data = []
    length = 0

    # want to parse stream of binary number rows into N columns
    # N is length of first column
    with open(fname, 'r') as f:
        for row in f:
            length = len(row.strip())
            for digit in row.strip():
                data.append(int(digit))
    return (data, length)

def part1(dataIn):
    (data, length) = dataIn
    reshapeData = [[] for _ in range(length)]

    count = 0
    for val in data:
        reshapeData[count].append(val)
        count = count + 1
        if count == length:
            count = 0

    gamma = ''.join(['1' if sum(row)/len(row) > 0.5 else '0' for row in reshapeData])
    epsilon = ''.join(['0' if sum(row)/len(row) > 0.5 else '1' for row in reshapeData])

    return int(gamma, base=2) * int(epsilon, base=2), gamma, epsilon

def part2(fname):
    # getting the oxygen generator rating and the c02 scrubber rating
    # process of elimination

    (data, length) = readInput(fname)

    # oxygen
    candidates = []
    with open(fname, 'r') as f:
        for row in f:
            candidates.append(row.strip())

    for i in range(length):
        data = []
        for candidate in candidates:
            for digit in candidate.strip():
                data.append(int(digit))
        
        reshapeData = [[] for _ in range(length)]
        count = 0
        for val in data:
            reshapeData[count].append(val)
            count = count + 1
            if count == length:
                count = 0
        
        ones = len(list(filter(lambda val: val == 1, reshapeData[i])))
        zeros = len(list(filter(lambda val: val == 0, reshapeData[i])))

        if len(candidates) == 1:
            break

        if ones >= zeros:
            candidates = list(filter(lambda candidate: candidate[i] == '1', candidates))
        else:
            candidates = list(filter(lambda candidate: candidate[i] == '0', candidates))

    oxygen = int(''.join(candidates), base=2)

    # co2
    candidates = []
    with open(fname, 'r') as f:
        for row in f:
            candidates.append(row.strip())

    for i in range(length):
        data = []
        for candidate in candidates:
            for digit in candidate.strip():
                data.append(int(digit))
        
        reshapeData = [[] for _ in range(length)]
        count = 0
        for val in data:
            reshapeData[count].append(val)
            count = count + 1
            if count == length:
                count = 0
        
        ones = len(list(filter(lambda val: val == 1, reshapeData[i])))
        zeros = len(list(filter(lambda val: val == 0, reshapeData[i])))

        if len(candidates) == 1:
            break

        if ones < zeros:
            candidates = list(filter(lambda candidate: candidate[i] == '1', candidates))
        else:
            candidates = list(filter(lambda candidate: candidate[i] == '0', candidates))
        print(candidates)

    co2 = int(''.join(candidates), base=2)
    
    return oxygen * co2

if __name__ == "__main__":
    solutionp1, gamma, epsilon = part1(readInput('sample.txt'))
    print(solutionp1)

    print(part2('input.txt'))