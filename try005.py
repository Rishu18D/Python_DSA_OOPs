#Selection Sorting
a=[7,35,69,734,34,5,3,47,56,37,4]
print("This is the unsorted list provided:",a)
for i in range(len(a)):
 min_value=min(a[i:])
 min_index=a.index(min_value)
 a[i],a[min_index]= a[min_index],a[i]
print("This is the Selection sort list:",a)