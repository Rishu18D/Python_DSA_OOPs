def list_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + list_sum(arr[1:])
print(list_sum([1, 2, 3, 4, 5]))