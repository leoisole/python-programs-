maxnoofrow = 4
maxnoofcol = 4
#data = [[1,1,1,0,0,0,1],[0,0,1,0,0,0,1],[1,1,1,1,1,1,1],[0,0,0,0,1,0,1],[1,1,1,1,1,0,1]]

data = [[1,1,1,0],[0,0,1,0],[1,1,1,0],[1,0,0,0]]

currentnode = [3,0] #node where we are.
previousnode = [3,0] #from where we have come .
savednode = []
actualpath = []
nodefound = [[]]
newnode = 0

def pathfinder(row,col):
    global currentnode, previousnode ,actualpath , nodefound , newnode

    print(nodefound,'nodefound')
    print(savednode,'savednode')

    if currentnode == [0,0] :
        print('done')
        return 0

    newnode = 0

    print(actualpath,'check')
    if row != 0 :
        if data[row-1][col] == 1 :
            if  previousnode != [row-1,col]:
                newnode += 1
                nodefound[-1].append([row-1,col])
                actualpath.append("U")

    if row != maxnoofrow-1 :
        if data[row+1][col] == 1 :
            if previousnode != [row + 1, col]:
                newnode += 1
                nodefound[-1].append([row + 1, col])
                actualpath.append("D")

    if col != 0 :
        if data[row][col-1] == 1 :
            if previousnode != [row,col-1]:
                newnode += 1
                nodefound[-1].append([row, col-1])
                actualpath.append("L")

    if col != maxnoofcol -1 :
        if data[row][col+1] == 1 :
            if previousnode != [row, col+1]:
                newnode += 1
                nodefound[-1].append([row, col+1])
                actualpath.append("R")

    if newnode > 1 :
        print(currentnode,'currentnode')
        savednode.insert(-1,currentnode)
        previousnode = currentnode
        currentnode = nodefound[-1][-1]
        nodefound[-1].pop(-1)
        # recursion code here
        pathfinder(currentnode[0],currentnode[1])


    if newnode == 0 :
        if nodefound[-1] == [] :
            nodefound.pop(-1)
            savednode.pop(-1)
            previousnode = savednode[-1]
            #nodefound[-1].pop(-1)
            pathfinder(currentnode[0], currentnode[1])

        elif nodefound[-1] != [] :
            previousnode = currentnode
            currentnode = nodefound[-1][-1]
            nodefound[-1].pop(-1)
            #recursion code here
            pathfinder(currentnode[0], currentnode[1])


    if newnode == 1 :
        previousnode = currentnode
        currentnode = nodefound[-1][-1]
        nodefound[-1].pop(-1)
        # recursion code here
        pathfinder(currentnode[0], currentnode[1])



a = pathfinder(3,0)

print(actualpath,'final')
