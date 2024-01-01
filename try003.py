#python program to find target value from adding two numbers of a list.
list1=[1,2,3,4,5,6,7,8,9,0]
target=8
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] +list1[j]==target:
           print(f"the target: ({list1[i]}),({list1[j]})")