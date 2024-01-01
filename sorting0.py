#Sorting algorithm...
def bubble(arr):
    n=len(arr)
    for i  in range(n):
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
              arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
def selection(ar):
    n=len(ar)
    for  i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if ar[j]<ar[min_idx]:
                min_idx=j
        ar[i],ar[min_idx]=ar[min_idx],ar[i]      
    return ar
def insertion(arr0):
    for i in range(1, len(arr0)):
        key = arr0[i]
        j = i-1
        while j >= 0 and key < arr0[j]:
            arr0[j + 1] = arr0[j]
            j -= 1
        arr0[j + 1] = key
    return arr0
arr=ar=arr0=[3,879,45,62,93,874,32,4,5]
result0=bubble(arr)
result1=selection(ar)
result2=insertion(arr0)
print("The Bubble sorting of fucking array is: ",result0)
print("The Selection sorting of fucking array is:",result1)
print("The Insertion sorting of fucking array is:",result2)
                              