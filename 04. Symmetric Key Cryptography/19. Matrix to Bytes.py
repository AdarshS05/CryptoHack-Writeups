state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrix2bytes(matrix):
    s=""
    for i in range (len(matrix)):
        t= (bytes(matrix[i])).decode("utf-8")
        s+=t
    return s

def add_round_key(s, k):
    for i in range (0,len(state)):
        for j in range (0,len(state[i])):
            state[i][j]=state[i][j]^round_key[i][j]
    return matrix2bytes(state)

print(add_round_key(state, round_key))

