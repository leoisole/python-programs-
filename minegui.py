from tkinter import *
import tkinter.messagebox as msg
import random

global size

root = Tk()

def minebase(size,noofbomb):
    global noofmine
    noofmine = noofbomb
    global width
    width = size
    global data
    data = []

    # making the base
    for i in range(size):
        data.append([])
        for j in range(size):
            data[i].append(0)

    for i in data:
        for j in i:
          print(j, end="|")
        print("\n")


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

    for i in data:
        for j in i:
          print(j, end="|")
        print("\n")

#checking player input
global box
def playgame(size):
    play = Tk()
    play.title("play mine")
    global box
    box = []






    for i in range(size):
        box.append([])
        for j in range(size):
            b = Button(play,None, text="" , bg = 'Grey',command=lambda i=i,j=j: chance(i,j))
            b.bind("<Button-3>",lambda event, i=i,j=j: flags(event,i,j))
            b.grid(row=i,column=j)
            box[i].append(b)



    print(list)


#player view ...game started


def chance(row,col):

    win = 0
    loss = 0
    global width
    global box
    global flag
    flag = 0

    def won():
        item = 0  # each element of the space.
        repeat = 0
        while (item < (width * width)):
            for i in range(width):
                if repeat == 0:
                    for j in range(width):
                        item += 1

                        if box[i][j]["text"] == "" or box[i][j]["text"] == "?" or box[i][j]["text"] == "@":
                            print("check")
                            if data[i][j] != '*':
                                repeat = 1
                                return

        if item == (width * width):
            for a in range(width) :
                for b in range(width):
                    box[a][b]["text"] = data[a][b]
                    box[a][b].config(bg="White", fg="Blue")
            msg.showinfo("lost", "Congratulations!!  , YOU WON ..LUCKY FELLOW. :)")

            global win
            win = 1

        return

    while (win == 0 and loss == 0):



        if data[row][col] == '*':
            for a in range(width) :
                for b in range(width):
                    box[a][b]["text"] = data[a][b]
                    box[a][b].config(bg="White", fg="Red")
            msg.showinfo("lost","Oops!! you lost! :(  Better luck next time.")
            loss = 1


        else:

            if data[row][col] == 0:
                box[row][col]["text"] = data[row][col]
                box[row][col].config(bg="White", fg="Red")


                def mine(row, col):
                    

                    if ((row != 0) and (col != 0)):
                        if ((data[row - 1][col - 1] != '*') and (box[row - 1][col - 1]["text"] == "")):
                            box[row - 1][col - 1]["text"] = data[row - 1][col - 1]
                            box[row - 1][col - 1].config(bg="White",fg="Red")

                            if box[row - 1][col - 1]["text"] == 0:
                                mine(row - 1, col - 1)

                    if (row != 0):
                        if ((data[row - 1][col] != '*') and (box[row - 1][col - 1]["text"] == "")):
                            box[row - 1][col]["text"] = data[row - 1][col]
                            box[row-1][col].config(bg="White",fg="Red")
                            if box[row - 1][col]["text"] == 0:
                                mine(row - 1, col)

                    if ((row != 0) and (col != width - 1)):
                        if ((data[row - 1][col + 1] != '*') and (box[row - 1][col + 1]["text"] == "")):
                            box[row - 1][col + 1]["text"] = data[row - 1][col + 1]
                            box[row-1][col+1].config(bg="White",fg="Red")
                            if box[row - 1][col + 1]["text"] == 0:
                                mine(row - 1, col + 1)

                    if (col != 0):
                        if ((data[row][col - 1] != '*') and (box[row][col - 1]["text"] == "")):
                            box[row][col - 1]["text"] = data[row][col - 1]
                            box[row][col-1].config(bg="White",fg="Red")
                            if box[row][col - 1]["text"] == 0:
                                mine(row, col - 1)

                    if (col != width - 1):
                        if ((data[row][col + 1] != '*') and (box[row][col + 1]["text"] == "")):
                            box[row][col + 1]["text"] = data[row][col + 1]
                            box[row][col+1].config(bg="White",fg="Red")
                            if box[row][col + 1]["text"] == 0:
                                mine(row, col + 1)

                    if ((row != width - 1) and (col != 0)):
                        if ((data[row + 1][col - 1] != '*') and (box[row + 1][col - 1]["text"] == "")):
                            box[row + 1][col - 1]["text"] = data[row + 1][col - 1]
                            box[row+1][col-1].config(bg="White",fg="Red")
                            if box[row + 1][col - 1]["text"] == 0:
                                mine(row + 1, col - 1)

                    if (row != width - 1):
                        if ((data[row + 1][col] != '*') and (box[row + 1][col]["text"] == "")):
                            box[row + 1][col]["text"] = data[row + 1][col]
                            box[row+1][col].config(bg="White",fg="Red")
                            if box[row + 1][col]["text"] == 0:
                                mine(row + 1, col)

                    if ((row != width - 1) and (col != width - 1)):
                        if ((data[row + 1][col + 1] != '*') and (box[row + 1][col + 1]["text"] == "")):
                            box[row + 1][col + 1]["text"] = data[row + 1][col + 1]
                            box[row+1][col+1].config(bg="White",fg="Red")
                            if box[row + 1][col + 1]["text"] == 0:
                                mine(row + 1, col + 1)

                    return 0

                mine(row, col)
                won()
                return

               





            else:

                box[row][col]["text"] = data[row][col]
                box[row][col].config(bg="White",fg="Red")
                won()
                return




ll = 0
def flags(event,x,y):
    global ll
    print(noofmine,"noofmine")

    if ll <= noofmine:
        box[x][y]["text"] = "@"
        ll = ll + 1
        box[x][y].config(bg="White", fg="Red")
    else:
        box[x][y]["text"] = '?'
        box[x][y].config(bg="White", fg="Red")










root.title("mine")

thelabel = Label(root, text="WELCOME TO MINE!!" , fg = 'Red')
thelabel.pack()

thelabel2 = Label(root, text="Made by LEO ;) " , fg = 'Green')
thelabel2.pack(side= BOTTOM)

topframe = Frame(root)
topframe.pack()

botframe = Frame(root)
botframe.pack(side=BOTTOM)





def but1(event):
    minebase(8,8)
    playgame(8)

def but2(event):
    minebase(10,10)
    playgame(10)

def but3(event):
    minebase(12,15)
    playgame(12)



def create():
    def evaluate():
        global sizes
        global bomb
        sizeinfo = sizes.get()
        bombinfo = bomb.get()
        minebase(int(sizeinfo), int(bombinfo))
        playgame(int(sizeinfo))

    base = Tk()
    base.title("custom mine")

    labelsize = Label(base,text= "Enter the size : ")
    labelsize.grid(row=0, column=0,sticky='E')
    global sizes
    sizes = Entry(base)
    sizes.grid(row=0,column=1)
    labelbomb = Label(base,text= "Enter the no. of bomb : ")
    labelbomb.grid(row=1, column=0)
    global bomb
    bomb = Entry(base)
    bomb.grid(row=1, column=1)

    enter = Button(base,text="Enter the values ",command=evaluate)
    enter.grid(row=2)





button1 = Button(topframe, text="size = 8*8 and mine = 8" , bg = 'Grey', fg = 'Blue')
button1.bind("<Button-1>",but1)
button1.pack(side = LEFT, fill = X)

button2 = Button(topframe, text="size = 10*10 and mine = 10" , bg = 'Grey', fg = 'Blue')
button2.bind("<Button-1>",but2)
button2.pack(side=RIGHT)

button3 = Button(botframe, text="size = 12*12 and mine = 15" , bg = 'Grey', fg = 'Blue')
button3.bind("<Button-1>",but3)
button3.pack(side = LEFT, fill = X)

button4 = Button(botframe, text="create your own minebase." , bg = 'Grey', fg = 'Blue' , command=create)

button4.pack(side = RIGHT, fill = Y)


root.mainloop()