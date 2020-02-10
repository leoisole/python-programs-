import random

chance = 0
loss = 0
box = 0

print('WELCOME TO NEW MINES GAME!!!')
print('PLEASE, ENTER THE ROW AND COLUMN VALUES TO PLAY.')

size = int(input("enter the size of minebas : "))
data = []

# making the base
for i in range(size):
    data.append([])
    for j in range(size):
        data[i].append(0)

# for i in data:
#     for j in i:
#         print(j, end="|")
#     print("\n")


noofbomb = int(input('Enter the number of mines.: '))

bombdata = []  # place where mine has to be planted.

# mmines coordinates

ichoice = []
jchoice = []

for i in range(size):
    ichoice.append(i)
    jchoice.append(i)

count = 0
choice = 0

# creating different mine location

while (len(bombdata) != noofbomb):

    x = random.choice(ichoice)
    y = random.choice(jchoice)

    if count == 0:
        bombdata.append([x, y])
        count += 1
        continue
    choice = 0

    for j in bombdata:
        if (j != [x, y]):
            choice += 1

    if choice == len(bombdata):
        bombdata.append([x, y])
        continue

# planting the bomb and updating data.

for i in bombdata:
    data[i[0]][i[1]] = '*'

    if ((i[0] != 0) and (i[1] != 0)):
        if (data[i[0] - 1][i[1] - 1] != '*'):
            data[i[0] - 1][i[1] - 1] = int(data[i[0] - 1][i[1] - 1]) + 1
    if (i[0] != 0):
        if (data[i[0] - 1][i[1]] != '*'):
            data[i[0] - 1][i[1]] = int(data[i[0] - 1][i[1]]) + 1
    if ((i[0] != 0) and (i[1] != size - 1)):
        if (data[i[0] - 1][i[1] + 1] != '*'):
            data[i[0] - 1][i[1] + 1] = int(data[i[0] - 1][i[1] + 1]) + 1
    if (i[1] != 0):
        if (data[i[0]][i[1] - 1] != '*'):
            data[i[0]][i[1] - 1] = int(data[i[0]][i[1] - 1]) + 1
    if (i[1] != size - 1):
        if (data[i[0]][i[1] + 1] != '*'):
            data[i[0]][i[1] + 1] = int(data[i[0]][i[1] + 1]) + 1
    if ((i[0] != size - 1) and (i[1] != 0)):
        if (data[i[0] + 1][i[1] - 1] != '*'):
            data[i[0] + 1][i[1] - 1] = int(data[i[0] + 1][i[1] - 1]) + 1
    if (i[0] != size - 1):
        if (data[i[0] + 1][i[1]] != '*'):
            data[i[0] + 1][i[1]] = int(data[i[0] + 1][i[1]]) + 1

    if ((i[0] != size - 1) and (i[1] != size - 1)):
        if (data[i[0] + 1][i[1] + 1] != '*'):
            data[i[0] + 1][i[1] + 1] = int(data[i[0] + 1][i[1] + 1]) + 1

# for i in data:
#   for j in i:
#      print(j, end="|")
# print("\n")


# from player view
global show
show = []

# making the base
for i in range(size):
    show.append([])
    for j in range(size):
        show[i].append('-')

for i in show:
    for j in i:
        print(j, end="|")
    print("\n")


# PRINT FUNCTION
def open():
    for i in show:
        for j in i:
            print(j, end="|")
        print("\n")
    print("---" * size)


win = 0

global flag
flag = 0


def won():
    box = 0  # each element of the space.
    repeat = 0
    while (box < (size * size)):
        for i in range(size):
            if repeat == 0:
                for j in range(size):
                    box += 1

                    if show[i][j] == '-' or show[i][j] == '?' or show[i][j] == '@':
                        if data[i][j] != '*':
                            repeat = 1

                            return

    if box == (size * size):
        print('CONGRATULATIONS , YOU WON ..LUCKY FELLOW. :) ')
        global win
        win = 1

    return


while (win == 0 and loss == 0):

    row = int(input("Enter the row value : "))
    col = int(input("Enter the col value : "))
    foundmine = int(input('FOUND ANY MINES ,yes = 1 , no = 0 : '))

    if foundmine == 1:
        x = 0
        y = 0
        x = int(input("Enter the row value : "))
        y = int(input("Enter the col value : "))
        if flag != noofbomb:
            show[x][y] = '@'
            flag += 1
        else:
            show[x][y] = '?'

        open()

    if data[row][col] == '*':
        show = data
        print('you lost! :(')
        loss = 1
        open()

    else:

        if data[row][col] == 0:
            show[row][col] = data[row][col]


            def mine(row, col):
                open()

                if ((row != 0) and (col != 0)):
                    if ((data[row - 1][col - 1] != '*') and (show[row - 1][col - 1] == '-')):
                        show[row - 1][col - 1] = data[row - 1][col - 1]

                        if show[row - 1][col - 1] == 0:
                            mine(row - 1, col - 1)

                if (row != 0):
                    if ((data[row - 1][col] != '*') and (show[row - 1][col - 1] == '-')):
                        show[row - 1][col] = data[row - 1][col]
                        if show[row - 1][col] == 0:
                            mine(row - 1, col)

                if ((row != 0) and (col != size - 1)):
                    if ((data[row - 1][col + 1] != '*') and (show[row - 1][col + 1] == '-')):
                        show[row - 1][col + 1] = data[row - 1][col + 1]
                        if show[row - 1][col + 1] == 0:
                            mine(row - 1, col + 1)

                if (col != 0):
                    if ((data[row][col - 1] != '*') and (show[row][col - 1] == '-')):
                        show[row][col - 1] = data[row][col - 1]
                        if show[row][col - 1] == 0:
                            mine(row, col - 1)

                if (col != size - 1):
                    if ((data[row][col + 1] != '*') and (show[row][col + 1] == '-')):
                        show[row][col + 1] = data[row][col + 1]
                        if show[row][col + 1] == 0:
                            mine(row, col + 1)

                if ((row != size - 1) and (col != 0)):
                    if ((data[row + 1][col - 1] != '*') and (show[row + 1][col - 1] == '-')):
                        show[row + 1][col - 1] = data[row + 1][col - 1]
                        if show[row + 1][col - 1] == 0:
                            mine(row + 1, col - 1)

                if (row != size - 1):
                    if ((data[row + 1][col] != '*') and (show[row + 1][col] == '-')):
                        show[row + 1][col] = data[row + 1][col]
                        if show[row + 1][col] == 0:
                            mine(row + 1, col)

                if ((row != size - 1) and (col != size - 1)):
                    if ((data[row + 1][col + 1] != '*') and (show[row + 1][col + 1] == '-')):
                        show[row + 1][col + 1] = data[row + 1][col + 1]
                        if show[row + 1][col + 1] == 0:
                            mine(row + 1, col + 1)

                return 0


            mine(row, col)

            open()
            won()




        else:

            show[row][col] = data[row][col]

            won()
            open()







