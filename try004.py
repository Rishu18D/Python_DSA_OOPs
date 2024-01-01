#Bubble Sorting
list0=[3,24,87,46,10,94,56,23,87]
print("This is the list:",list0)
for j in range(len(list0)-1):
 for i in range(len(list0)-1):
    if list0[i]>list0[i+1]:
        list0[i],list0[i+1]= list0[i+1],list0[i]
print("Bubble shorted list:",list0)