def printmatrix(matrix):
    print(len(matrix), len(matrix[0]))
    string = ""
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            string = string + str(matrix[y][x]) + " "
        print(string)
        string = ""
