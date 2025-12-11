import json



with open("example.json", "r") as f:
    data = json.load(f)

N = data["grid_size"]["N"]
M = data["grid_size"]["M"]
MAP = data["map"]

# N, M = 7, 7  # Map Size
MR, MC = 0, 0
CR, CC = N - 1, M - 1
SRC_MOUSE = (MR, MC)

SRC_CAT=(CR,CC)

# MAP = []  # Map of the Game

DISTANCE_CAT = {}  # Distances
DISTANCE_MOUSE={}
PARENT = {}    # Parents

DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]


def Check_Goal(i, j):
    return MAP[i][j] == 'G'


def BFS_CAT(SRC: tuple):
    Q = [SRC]
    DISTANCE_CAT[SRC] = 0

    while Q:
        I, J = Q.pop(0)

        for k in range(4):
            newi = I + DX[k]
            newj = J + DY[k]

            if 0 <= newi < N and 0 <= newj < M:

                if MAP[newi][newj] == '#':
                    continue

                new_T = (newi, newj)

                if new_T not in DISTANCE_CAT:
                    DISTANCE_CAT[new_T] = DISTANCE_CAT[(I, J)] + 1
                    Q.append(new_T)


def BFS_MOUSE(SRC: tuple):
    Q = [SRC]
    DISTANCE_MOUSE[SRC] = 0

    while Q:   
        I, J = Q.pop(0)

        if Check_Goal(I, J):
            return "Path Found"

        for k in range(4):
            newi = I + DX[k]  
            newj = J + DY[k]   

            if 0 <= newi < N and 0 <= newj < M:  

                if MAP[newi][newj] == '#':
                    continue

                new_T = (newi, newj)

                # Not visited
                if new_T not in DISTANCE_MOUSE: 

                    # Cat MUST have a distance value for this cell
                    if new_T in DISTANCE_CAT:

                        # Mouse must reach earlier than cat
                        if DISTANCE_MOUSE[(I, J)] + 1 < DISTANCE_CAT[new_T]:

                            PARENT[new_T] = (I, J)
                            DISTANCE_MOUSE[new_T] = DISTANCE_MOUSE[(I, J)] + 1
                            Q.append(new_T)

    return "No Safe Path"


BFS_CAT(SRC=SRC_CAT)
State=BFS_MOUSE(SRC=SRC_MOUSE)
if State=='Path Found'  : 
    print("You Passed Mouse ALive!")
    
else : 
    print("No Safe Path Mouse died")