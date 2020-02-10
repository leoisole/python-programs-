data = "absh[hakjf(avdvj{ldfks}vnskj)nfvnk]"


    
stack = []
    

def push(stack,item):
    stack.append(item)
    print(stack)
    return

def pop(stack):
    stack.pop(0)
    return

def isempty(stack):
    if stack == [] :
        return True
    return False





n = len(data)
for ele in range(0,n,-1):
    if ele == "{" or "[" or "(" :
        push(stack,ele)


print(stack)








