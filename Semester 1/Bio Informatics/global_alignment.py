class Score:

    def __init__(self, gap, match, mismatch):
        self.gap = gap
        self.match = match
        self.mismatch = mismatch

    def mismatchchar(self, x, y):
        if x != y:
            return self.mismatch
        else:
            return self.match


def get_matrix(sizeX, sizeY, gap):
    matrix = []
    for i in range(len(sizeX)+1):
        subMatrix = []
        for j in range(len(sizeY)+1):
            subMatrix.append(0)
        matrix.append(subMatrix)

    for j in range(1, len(sizeY)+1):
        matrix[0][j] = j*gap

    for i in range(1, len(sizeX)+1):
        matrix[i][0] = i*gap

    return matrix

def get_tracebackMatrix(sizeX, sizeY):
    matrix = []
    for i in range(len(sizeX)+1):
        subMatrix = []
        for j in range(len(sizeY)+1):
            subMatrix.append(0)
        matrix.append(subMatrix)

    for j in range(1, len(sizeY)+1):
        matrix[0][j] = 'left'
    for i in range(1, len(sizeX)+1):
        matrix[i][0] = 'up'
    matrix[0][0] = 'done'

    return matrix

def global_align(x, y, score):
    matrix = get_matrix(x, y, score.gap)
    traceback = get_tracebackMatrix(x, y)

    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):

            left = matrix[i][j-1] + score.gap
            up = matrix[i-1][j] + score.gap
            diag = matrix[i-1][j-1] + score.mismatchchar(x[i-1], y[j-1])
            matrix[i][j] = max(left, up, diag)

            if matrix[i][j] == left:
                traceback[i][j] = 'left'
            elif matrix[i][j] == up:
                traceback[i][j] = 'up'
            else:
                traceback[i][j] = 'diag'

    for i in matrix:
        print(i)

    for j in traceback:
        print(j)



x='adc'
y='sss'
g = Score(-2, 1, -1)
global_align(x, y, g)
