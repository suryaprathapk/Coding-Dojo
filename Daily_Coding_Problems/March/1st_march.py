array1 = [10, 15, 3, 7]
b=[]
def Sum_up_to_input(Ksum):
    for i in range(len(array1)):
        b.append(array1[i])
        for j in range(i):
           if array1[i]+b[j] ==Ksum:
                return "true"
    return "false"
     

print(Sum_up_to_input (22))