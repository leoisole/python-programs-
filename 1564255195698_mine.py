import random



size = int(input("enter the size of minebas : "))
data = []

#making the base
for i in range(size) :
    data.append([])
    for j in range(size) :
        data[i].append(0)

for i in data:
    for j in i:
        print(j, end="|")
    print("\n")



noofbomb = int(input('Enter the number of mines.: '))

bombdata = [] #place where mine has to be planted.


#mmines coordinates

ichoice = []
jchoice = []

for i in range(size):
    ichoice.append(i)
    jchoice.append(i)


count = 0
choice = 0

#creating different mine location

while(len(bombdata) != noofbomb):

    x = random.choice(ichoice)
    y = random.choice(jchoice)

    if count == 0 :
        bombdata.append([x, y])
        count += 1
        continue
    choice = 0

    for j in bombdata :
        if (j != [x,y])  :
            choice += 1

    if choice == len(bombdata) :
        bombdata.append([x, y])
        continue


print(bombdata)

#planting the bomb and updating data.

for i in bombdata :
        data[i[0]][i[1]] = '*'


        if ((i[0] != 0 ) and (i[1] != 0 )) :
            if (data[i[0]-1][i[1]-1] != '*') :
                data[i[0]-1][i[1]-1] = int(data[i[0]-1][i[1]-1]) + 1
        if  (i[0] != 0 ) :
            if (data[i[0] - 1][i[1] ] != '*') :
                data[i[0]-1][i[1]]   = int( data[i[0]-1][i[1]] ) + 1
        if  ((i[0] != 0 ) and (i[1] != size -1)) :
            if (data[i[0] - 1][i[1] + 1] != '*')  :
                data[i[0]-1][i[1]+1] = int(data[i[0]-1][i[1]+1])+1
        if (i[1] != 0 ) :
            if (data[i[0] ][i[1] - 1] != '*'):
                data[i[0]][i[1]-1]   = int(data[i[0]][i[1]-1] ) + 1
        if (i[1] != size -1) :
            if (data[i[0] ][i[1] + 1] != '*'):
              data[i[0]][i[1]+1]   = int(data[i[0]][i[1]+1]) + 1
        if ((i[0] != size-1 ) and (i[1] != 0 )):
            if (data[i[0] + 1][i[1] - 1] != '*') :
                data[i[0]+1][i[1]-1] = int(data[i[0]+1][i[1]-1]) + 1
        if (i[0] != size-1 ) :
            if (data[i[0] + 1][i[1]] != '*')  :
                data[i[0]+1][i[1]]   = int(data[i[0]+1][i[1]]) + 1

        if ((i[0] != size-1 ) and (i[1] != size-1)) :
            if (data[i[0] +1][i[1] + 1] != '*') :
                data[i[0]+1][i[1]+1] = int(data[i[0]+1][i[1]+1]) + 1



for i in data:
    for j in i:
        print(j, end="|")
    print("\n")


#from player view
show = []
#making the base
for i in range(size) :
    show.append([])
    for j in range(size) :
        show[i].append('-')

for i in show:
    for j in i:
        print(j, end="|")
    print("\n")


#PRINT FUNCTION
def open():
    for i in show:
        for j in i:
            print(j, end="|")
        print("\n")

chance = 0
win = 0
loss = 0

while (win == 0 or loss == 0 ) :
    row = int(input("Enter the row value : "))
    col = int(input("Enter the col value : "))

    if data[row][col] == '*' :
        show = data
        print('you lost! :(')
        loss = 1

        for i in show:
            for j in i:
                print(j, end="|")
            print("\n")

    else :



        if data[row][col]  == 0 :
            show[row][col] =  data[row][col]
            def mine(row,col):
                open()


                if ((row != 0 ) and (col != 0 )) :
                    if ((data[row-1][col-1] != '*') and ( show[row-1][col-1] == '-' )) :
                        show[row-1][col-1] = data[row-1][col-1]

                        if show[row-1][col-1] == 0 :

                            mine(row-1,col-1)
                            open()



                if  (row != 0 ) :
                    if ((data[row - 1][col ] != '*') and ( show[row-1][col-1] == '-')) :
                        show[row-1][col]   =  data[row-1][col] 
                        if show[row-1][col] == 0 :

                            mine(row-1,col)
                            open()

                
                if  ((row != 0 ) and (col != size -1)) :
                    if ((data[row - 1][col + 1] != '*') and ( show[row-1][col+1] == '-'))  :
                        show[row-1][col+1] = data[row-1][col+1]
                        if show[row-1][col+1] == 0 :

                            mine(row-1,col+1)
                            open()

                
                if (col != 0 ) :
                    if ((data[row ][col - 1] != '*') and ( show[row][col-1] == '-')):
                        show[row][col-1]   = data[row][col-1]  
                        if show[row][col-1] == 0 :

                            mine(row,col-1)
                            open()

                
                if (col != size -1) :
                    if ((data[row ][col + 1] != '*') and ( show[row][col+1] == '-')):
                        show[row][col+1]   = data[row][col+1]
                        if show[row][col+1] == 0 :

                            mine(row,col+1)
                            open()

                if ((row != size-1 ) and (col != 0 )):
                    if ((data[row + 1][col - 1] != '*') and ( show[row+1][col-1] == '-')) :
                        show[row+1][col-1] = data[row+1][col-1]
                        if show[row+1][col-1] == 0 :

                            mine(row+1,col-1)
                            open()

                
                if (row != size-1 ) :
                    if ((data[row + 1][col] != '*') and ( show[row+1][col] == '-')  ):
                        show[row+1][col]   = data[row+1][col] 
                        if show[row+1][col] == 0 :

                            mine(row+1,col)
                            open()


                if ((row != size-1 ) and (col != size-1)) :
                    if ((data[row +1][col + 1] != '*') and ( show[row+1][col+1] == '-')) :
                        show[row+1][col+1] = data[row+1][col+1]
                        if show[row+1][col+1] == 0 :

                            mine(row+1,col+1)
                            open()


                return 0

            mine(row,col)

            open()





        elif True  :
            show[row][col] =  data[row][col]

            open()

        else :
            print('CONGRATULATIONS , YOU WON ..LUCKY FELLOW. :) ')





