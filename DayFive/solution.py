# Advent of Code Day 5
# Patrick Johnson 2021

# hydrothermal vent problem
# or, infinite grid

def readInput(fname):
    # return a list of lines
    data = []

    # sort so that start is always smaller than end
    with open(fname) as f:
        for line in f:
            line = line.strip()
            start, end = line.split(' -> ')
            x1, y1 = start.split(',')
            x2, y2 = end.split(',')
            data.append({'start' : (int(x1), int(y1)), 'end' : (int(x2), int(y2))})
    
    return data

def vertical(line):
    return line['start'][0] == line['end'][0]

def horizontal(line):
    return line['start'][1] == line['end'][1]

def getPoints(start, end):
    points = []
    if start[0] < end[0]:
        xIncrement = 1
    elif start[0] > end[0]:
        xIncrement = -1
    elif start[0] == end[0]:
        xIncrement = 0
    if start[1] < end[1]:
        yIncrement = 1
    elif start[1] > end[1]:
        yIncrement = -1
    elif start[1] == end[1]:
        yIncrement = 0

    point = start
    points.append(point)
    while point != end:
        point = (point[0] + xIncrement, point[1] + yIncrement)
        points.append(point)

    return points

def part1(data):
    # figure out the number of points which have more than 1 hydrothermal vent
    points = {}
    for line in data:
        # do nothing if the line is not vertical or horizontal
        #print(f"vertical or horizontal: {vertical(line) or horizontal(line)} for line {line}")
        if vertical(line) or horizontal(line):
            # construct list of tuples of x,y points to update in points
            for point in getPoints(line['start'], line['end']):
                if point in points.keys():
                    points[point] = points[point] + 1
                else:
                    points.update({point : 1})
    
    numOverlap = 0
    for point, count in points.items():
        if count > 1:
            numOverlap = numOverlap + 1
    
    return numOverlap

def part2(data):
    # same as part 1, but also consider lines that are diagonal (45 deg)
    points = {}
    for line in data:
        for point in getPoints(line['start'], line['end']):
            if point in points.keys():
                points[point] = points[point] + 1
            else:
                points.update({point : 1})
    
    numOverlap = 0
    for point, count in points.items():
        if count > 1:
            numOverlap = numOverlap + 1
    
    return numOverlap

if __name__ == "__main__":
    #data = readInput('sample.txt')
    data = readInput('input.txt')

    solution_1 = part1(data)
    print(solution_1)

    solution_2 = part2(data)
    print(solution_2)