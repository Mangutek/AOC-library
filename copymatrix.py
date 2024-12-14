def copymatrix(new, old):
    for z in range(len(old)):
        new.append([])
    for y in range(len(old)):
        for x in range(len(old[y])):
             new[y].append(old[y][x])

def copylist(new, old):
    for elem in old:
        new.append(elem)