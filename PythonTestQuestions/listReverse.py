list = [1,2,3,4,5]

length=len(list)

list2=[]

for i in range(length):
    a = list[length-1]
    list2.append(a)
    length += -1

print(list2)

    
    