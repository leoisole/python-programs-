data = [7,3,1,4,2,5]
inputs = []

def median():
    global input
    length = len(inputs)
    print(length)

    if length % 2 == 0 :
        firstindex = (length/2) - 1
        secondindex = length / 2

        median = (inputs[int(firstindex)] + inputs[int(secondindex)]) / 2 
        return median
    
    else:
        index = (length + 1 ) / 2
        index -= 1
        median = inputs[int(index)]
        return median


for i in range(0,len(data),1):
    inputs.append(data[i])
    print(inputs)
    print(median())

