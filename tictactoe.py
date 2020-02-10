import random
print("welcome to tictactoe. \n YOU are  '*' & Bot is '0'.")

print("instruction - please enter row val first & then column value.")

print("\n you  will start first.")

data = [['-','-','-'],['-','-','-'],['-','-','-']]

flag = 0

	
def bot(p1):
        if count == 1 :
                
                
                #center
                center = ['1','1']
                l = []
                if p1 == center :
                
                    for i in range(3):
                        for j in range(3):
                            l.append([i,j])
                    
                    l.remove([1,1])
                    p2 = random.choice(l)
                    return(p2)
                #corner

                cor = [['0','0'],['2','2'],['0','2'],['2','0']]
                if p1 == cor[0] :
                
                    l.append([int(p1[0])+1,int(p1[1])])
                    l.append([int(p1[0])+2,int(p1[1])])
                    l.append([int(p1[0]),int(p1[1])+1])
                    l.append([int(p1[0]),int(p1[1])+2])
                    l.append([1,1])
                    l.append([2,2])
                    p2 = random.choice(l)
                    return(p2)
                if p1 == cor[1] :
                
                    l.append([int(p1[0])-1,int(p1[1])])
                    l.append([int(p1[0])-2,int(p1[1])])
                    l.append([int(p1[0]),int(p1[1])-1])
                    l.append([int(p1[0]),int(p1[1])-2])
                    l.append([1,1])
                    l.append([0,0])
                    p2 = random.choice(l)
                    return(p2)

                if p1 == cor[2] :
                
                    l.append([int(p1[0])+1,int(p1[1])])
                    l.append([int(p1[0])+2,int(p1[1])])
                    l.append([int(p1[0]),int(p1[1])-1])
                    l.append([int(p1[0]),int(p1[1])-2])
                    l.append([1,1])
                    l.append([2,0])
                    p2 = random.choice(l)
                    return(p2)
                if p1 == cor[3] :
                
                    l.append([int(p1[0])-1,int(p1[1])])
                    l.append([int(p1[0])-2,int(p1[1])])
                    l.append([int(p1[0]),int(p1[1])+1])
                    l.append([int(p1[0]),int(p1[1])+2])
                    l.append([1,1])
                    l.append([0,2])
                    p2 = random.choice(l)
                    return(p2)

               			

                #edge
                edge = [['0','1'],['2','1'],['1','0'],['1','2']]


                if p1 == edge[0] :

                    l.append([int(p1[0]),int(p1[1])-1])
                    l.append([int(p1[0]),int(p1[1])+1])
                    l.append([int(p1[0])+1,int(p1[1])])
                    l.append([int(p1[0])+2,int(p1[1])])
                    p2 = random.choice(l)
                    return(p2)
                if p1 == edge[1] :
                
                    l.append([int(p1[0]),int(p1[1])-1])
                    l.append([int(p1[0]),int(p1[1])+1])
                    l.append([int(p1[0])-1,int(p1[1])])
                    l.append([int(p1[0])-2,int(p1[1])])
                    p2 = random.choice(l)
                    return(p2)
                if p1 == edge[2] :

                    l.append([int(p1[0])-1,int(p1[1])])
                    l.append([int(p1[0])+1,int(p1[1])])
                    l.append([int(p1[0]),int(p1[1])+1])
                    l.append([int(p1[0]),int(p1[1])+2])
                    p2 = random.choice(l)
                    return(p2)
                if p1 == edge[3] :

                    l.append([int(p1[0])-1,int(p1[1])])
                    l.append([int(p1[0])+1,int(p1[1])])
                    l.append([int(p1[0]),int(p1[1])+1])
                    l.append([int(p1[0]),int(p1[1])+2])
                    p2 = random.choice(l)
                    return(p2)
        flag = 0
	#row
        for i in range(3) :
            
        
            if data[i][0] == data[i][1] == "0" or data[i][1] == data[i][2] == "0" or data[i][0] == data[i][2] == "0" :
                for j in range(3) :		
                    if data[i][j] == "-" :
                        p2 = [i,j]
                        return(p2)
                        flag = 1
        for i in range(3) :
            if data[i][0] == data[i][1] == "*" or data[i][1] == data[i][2] == "*" or data[i][0] == data[i][2] == "*":
                for j in range(3) :		
                    if data[i][j] == "-" :
                        p2 = [i,j]
                        return(p2)
                        flag = 1
        #column
        for j in range(3) :
            
            if data[0][j] == data[1][j] == "0" or data[2][j] == data[1][j] == "0" or data[0][j] == data[2][j] == "0" :
                for i in range(3) :		
                    if data[i][j] == "-" :
                        p2 = [i,j]
                        return(p2)
                        flag = 1 
        for j in range(3) :
            if data[0][j] == data[1][j] == "*" or data[1][j] == data[2][j] == "*" or data[0][j] == data[2][j] == "*":
                for i in range(3) :		
                    if data[i][j] == "-" :
                        p2 = [i,j]
                        return(p2)
                        flag = 1

        #diagonal

        if data[1][1] == data[2][2] == "0" or data[0][0] == data[2][2] == "0" or data[1][1] == data[0][0] == "0" :
            for i in range(3) :		
                if data[i][i] == "-" :
                    p2 = [i,i]
                    return(p2)
                    flag = 1
        if data[1][1] == data[2][2] == "*" or data[0][0] == data[2][2] == "*" or data[1][1] == data[0][0] == "*" :
            for i in range(3) :		
                if data[i][i] == "-" :
                    p2 = [i,i]
                    return(p2)
                    flag = 1

        if data[2][0] == data[1][1] == "0" or data[1][1] == data[0][2] == "0" or data[0][2] == data[2][0] == "0" :
            l = [[2,0],[1,1],[0,2]]
            for i in l :		
                if data[int(i[0])][int(i[1])] == "-" :
                    p2 = i
                    return(p2)
                    flag = 1
        if data[2][0] == data[1][1] == "*" or data[1][1] == data[0][2] == "*" or data[0][2] == data[2][0] == "*" :
            l = [[2,0],[1,1],[0,2]]
            for i in l :	
                if data[int(i[0])][int(i[1])] == "-" :
                    p2 = i
                    return(p2)
                    flag = 1
        
        
        for i in range(3) :
            for j in range(3) :
                if data[i][j] == "-" and flag == 0 :
                    p2 = [i,j]
                    return(p2)
                    flag = 1
                                        
		
#Deciding which player wins.
win = 0 
w = 0		

def winner(a):
	
	win = 0 
	w = 0
	#condion 1 : row match

	for i in range(3):
	
		if data[i][0] == data[i][1] == data[i][2] == '*' :
			print("player 1 wins.")
			win = 1
		
	for i in range(3):	
		if win == 0 :
			if data[i][0] == data[i][1] == data[i][2] == '0' :
				print("player 2 wins.")
				w = 1
	#condion 2 : column match

	for j in range(3):
	
		if data[0][j] == data[1][j] == data[2][j] == '*' :
			print("player 1 wins.")
			win = 1
	for j in range(3):	
		if win == 0 :
			if data[0][j] == data[1][j] == data[2][j] == '0' :
				print("player 2 wins.")
				w = 1
	#condion 1 : diagonal match

	if data[0][0] == data[1][1] == data[2][2] == '*' or data[0][2] == data[1][1] == data[2][0] == '*' :
			print("player 1 wins.")
			win = 1

	if win == 0 :
		if data[0][0] == data[1][1] == data[2][2] == '0' or data[0][2] == data[1][1] == data[2][0] == '0' :
			print("player 2 wins.")
			w = 1
	if win != 1 and  w != 1 and count == 9: 
		print("\n MATCH DRAW")
		return(0)
	if win ==1 or w == 1 :
		return(1)
	

	



# Function to print the input .

def fill(row,col,val):
    if val == 1 :

        data[row][col] = '*'
        for i in data:
            for j in i :	
                print(j,end="")
            print("\n")
    print("---------")
    if val == 2 :
        data[row][col] = '0'
        for i in data:
            for j in i :
                print(j,end="")
            print("\n")

#taking the player input & calling fill function.
count = 0
a = 0
for i in range(5) :
    if  win == 0 and w == 0 and (a == 0 or a == None) :
        p1 = []
        p2 = []
            
        for j in range(2):
            p1.append(input("enter the value: "))
            print(p1)
        fill(int(p1[0]),int(p1[1]),1)
        count = count + 1
        if count >= 5 :
            a = winner(0)
        if a != 1 :
            p2 = bot(p1)
            
        fill(int(p2[0]),int(p2[1]),2)
        count = count + 1
		

	
        if count == 9 and (a == 0 or a == None)  :    
            a = winner(0)
                
		
		




