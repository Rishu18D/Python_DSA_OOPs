def binary_search(arr, target):
    if not arr:
        return -1
    else:
        mid = len(arr) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr[:mid], target)
        else:
            result = binary_search(arr[mid + 1:], target)
            if result == -1:
                return -1
            return mid + 1 + result
arr=(1,2,3,4,5,6,7,8,9,10)        
print(binary_search(arr,6))