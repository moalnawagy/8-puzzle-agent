
import copy

goalPuzzle = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def get_Zero_pos(puzzele):
    pos = puzzele.index(0)
    return pos


def horizontal_available_moves(pos):
    if (pos%3 ==0):
        return ['>']
    elif (pos%3 ==2):
        return ['<']
    else:
        return ['<', '>']

def vertical_available_moves(pos):
    if pos <3:
        return ['v']
    elif pos <6:
        return ['v', '^']
    else:
        return ['^']

def possible_moves(puzzele):
    pos = get_Zero_pos(puzzele)
    vertical = vertical_available_moves(pos)
    horizontal = horizontal_available_moves(pos)
    return vertical + horizontal

    

def aplly_move(move,puzzle):
    temp = copy.copy(puzzle)
    pos = get_Zero_pos(puzzle)
    if move == '^':
        temp[pos-3], temp[pos] = temp[pos], temp[pos-3]
    elif move == 'v':
        temp[pos+3], temp[pos] = temp[pos], temp[pos+3]
    elif move == '>':
        temp[pos+1], temp[pos] = temp[pos], temp[pos+1]
    elif move == '<':
        temp[pos-1], temp[pos] = temp[pos], temp[pos-1]
    return temp


def check_for_winning(puzzele):
    return puzzele == goalPuzzle


def compute_cost(state, action):
    new_state = aplly_move(state, action)
    cost = 0
    for i in range(9):
        if new_state[i] != i :
            cost +=1
    return cost
