# Python program to find how similar 2 strings are

def compute(x,y,a,b):
    """Computing a shit matrix!"""
    l = []

    # Deletion

    temp = matrix[x - 1][y][0] + 1
    l.append((temp,1))

    # Insertion
    temp = matrix[x][y - 1][0] + 1
    l.append((temp,2))

    # substitude

    if ( a[x-1] == b[y-1]):
        temp = matrix[x - 1][y - 1][0]
        l.append((temp,3))
    else:
        temp = matrix[x - 1][y - 1][0] + 1
        l.append((temp,3))


    if l[0][0] <= l[1][0] and l[0][0] <= l[2][0]:
        return l[0]
    elif l[1][0] <= l[2][0]:
        return l[1]
    else:
        return l[2]



def distances(a, b):
    """Calculate edit distance from a to b"""

    # TODO
    # DELETED = 1
    # INSERTED = 2
    # SUBSTITUTED = 3

    global matrix
    matrix = [ [(0,0) for x in range(len(b) + 1)] for x in range(len(a) + 1 ) ]

    for x in range(len(b) + 1):
        matrix[0][x] = (x,2)

    for x in range(len(a) + 1):
        matrix[x][0] = (x,1)

    matrix[0][0] = (0,0)

    # Computation
    for y in range(1,len(b) + 1):
        for x in range(1,len(a) + 1):
    	    matrix[x][y] = compute(x,y,a,b)

    for x in range(len(a) + 1):
        for y in range(len(b) + 1):
            print(str(matrix[x][y]) + " " ,end="")
        print()

    print("We can convert \"{}\" -> \"{}\" in {} minimum number of steps".format(a,b,matrix[len(a)][len(b)][0]))
    return matrix

distances("flyware","warefry")
