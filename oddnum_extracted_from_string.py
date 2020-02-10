a = input("enter the string: ")
print(a)
num = []
for i in a :
    if i.isnumeric() :
        num.append(i)

final = ['-1']
check = False
for i in num :
    count = 1  
    
    for j in final :
            check = False
            
            if int(i) != int(j) and count == len(final):
                
                check = True
            if i == j :
                break
            count += 1
            
            
    if check == True :
        final.append(i)
final.pop(0)


final.sort()

even = True
for i in final :
    if int(i) % 2 != 0 :
        even = False
        break
if even == True :
    print(-1)

if int(final[0]) == 0 :
    temp = final[0]
    final[0] = final[1]
    final[1] = temp

if even == False:
    if int(final[-1]) % 2 == 0 :
        for i in range(-1,-len(final),-1):
            
            if int(final[i]) % 2 != 0  :
                val = final[i]
                final.pop(i)
                final.append(val)
                for j in final :
                    print(j,end="")
                break

   
    
    
    
    

        
            
