string = "asbd]h(kfa{ldfjl}lkvjsl)ofd[12ads]"
stack = []

def isempty():
    if stack == [] :
        return True
    return False

def push(stack,ele):
    stack.append(ele)

def pop(stack):
    stack.pop()

fal = False

for i in range(0,len(string),1):
    print(stack,'stack[')
    #print(string[i],'sd')
    if string[i] == "(" or string[i] == "{" or string[i] == "[" :
        push(stack,string[i])
        continue

    if string[i] == ")" or string[i] == "}" or string[i] == "]" :
        if isempty() == False :
            if string[i] == "}":
                if stack[-1] == "{":
                    pop(stack)
                    continue
            if string[i] == ")":
                if stack[-1] == "(":
                    pop(stack)
                    continue 
            if string[i] == "]":
                if stack[-1] == "[":
                    pop(stack)
                    continue
        else :
            print("bahut faltu")
            fal = True
            break
if fal == False:
    if isempty() == True :
        print("String is proper.")

    else :
        print("Faltu string")
