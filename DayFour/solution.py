# Advent of Code Day 4
# Patrick Johnson 2021

# bingo

def readInput(fname):
    # bingo numbers and boards
    data = {'numbers': [], 'boards': []}

    row = 0
    count = 0
    board = []
    # first line is numbers to be called
    # following are sequences of 5x5 boards
    with open(fname) as f:
        for line in f:
            line = line.strip()
            if row == 0:
                data['numbers'] = line.split(',')
            elif line == '':
                pass
            else:
                board.append(list(filter(lambda x: x != '', line.split(' '))))
                count = count + 1
            if count == 5:
                data['boards'].append(board)
                board = []
                count = 0
            row = row + 1

    return data

def mark(board, number):
    for row in range(len(board)):
        for num in range(len(board[row])):
            if board[row][num] == number:
                board[row][num] = ''
    return board


def checkWin(board):
    win = False
    # check for any row that's all ''
    for row in board:
        if row == ['', '', '', '', '']:
            win = True
    # check for any column thats ''
    for i in range(5):
        if board[0][i] == '' and board[1][i] == '' and board[2][i] == ''and board[3][i] == ''and board[4][i] == '':
            win = True  

    return win


def part1(data):

    for number in data['numbers']:
        for board in data['boards']:
            board = mark(board, number)
            data['win'] = checkWin(board)
            if data['win']:
                newStream = []
                for row in board:
                    for char in row:
                        if char != '':
                            newStream.append(int(char))
                data['win'] = False
                return sum(newStream) * int(number)

def part2(data):
    # board number, score
    wins = {}
    for number in data['numbers']:
        for board in data['boards']:
            board = mark(board, number)
            if checkWin(board):
                newStream = []
                for row in board:
                    for char in row:
                        if char != '':
                            newStream.append(int(char))
                if data['boards'].index(board) not in wins.keys():
                    wins.update({data['boards'].index(board) : sum(newStream) * int(number)})
    
    return wins[list(wins.keys())[-1]]

if __name__ == "__main__":
    data = readInput('input.txt')
    print(part1(data))

    data = readInput('input.txt')
    print(part2(data))