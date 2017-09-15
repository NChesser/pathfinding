import copy

class Node(object):

    def __init__(self, x=0, y=0, walkable=True):
        self.x = x
        self.y = y

        self.walkable = walkable

    def __hash__(self):
        return hash(str(self.x)+":"+str(self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    
    def __repr__(self):
        return str(self.x) + ":" + str(self.y)

    
rows = 10
cols = 10

board = {Node(x,y):'0' for x in range(rows) for y in range(cols)}

board[Node(0,0)] = 'S'
board[Node(9,9)] = 'X'
board[Node(9,0)] = 'W'
board[Node(8,1)] = 'W'
board[Node(7,2)] = 'W'
board[Node(6,3)] = 'W'
#board[Node(5,4)] = 'W'
board[Node(4,5)] = 'W'
board[Node(3,6)] = 'W'
board[Node(2,7)] = 'W'
board[Node(1,8)] = 'W'
board[Node(0,9)] = 'W'

def is_goal(state):
    if board[state] != 'X':
        return False
    return True

def shortest_path_search(start):
    if is_goal(start):
        return start

    explored = set([start])
    frontier = [ [start, [start]] ]
    while frontier:
        path = frontier.pop(0)
        for (state, movement) in successors(path).items():
            if state not in explored:
                explored.add(state)
                #path2 = path + [action, state]
                if is_goal(state):
                    print(movement[1:6])
                    return movement[1:-1]

                frontier.append([state, movement])                       
    
    return []

def successors(statemovement):
    #If there are not enough free spaces to place a queen it should return nothing
    states = []  
    state, movement = statemovement
    
    # →
    if state.x < rows-1 and board[Node(state.x+1,state.y)] != 'W':
        s = copy.copy(state)
        s.x += 1
        m = movement.copy()
        m += [s]
        states += [(s, m)]
    # ←
    if state.x > 0 and board[Node(state.x-1,state.y)] != 'W':
        s = copy.copy(state)
        s.x -= 1
        m = movement.copy()
        m += [s]
        states += [(s, m)]
    # ↓   
    if state.y < cols-1 and board[Node(state.x,state.y+1)] != 'W':
        s = copy.copy(state)
        s.y += 1
        m = movement.copy()
        m += [s]
        states += [(s, m)]
    # ↑
    if state.y > 0 and board[Node(state.x,state.y-1)] != 'W':
        s = copy.copy(state)
        s.y -= 1
        m = movement.copy()
        m += [s]
        states += [(s, m)]

    return dict(states)

def print_board(movement):
    for m in movement:
        board[m] = '.'
    
    for r in range(rows):
        for c in range(cols):
            print(board[Node(r,c)], end=' '), 
        print()
    print()
    
print_board(shortest_path_search(Node(0,0)))

