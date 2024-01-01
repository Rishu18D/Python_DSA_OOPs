
            ###########################################################################

def find_pairs(arr, target_sub):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] - arr[j] == target_sub or arr[j] - arr[i] == target_sub:
                pairs.append((arr[i], arr[j]))
    return pairs

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sub = 3
result = find_pairs(arr, target_sub)
print("All the pairs whose subtraction is equal to", target_sub, "are:\n", result)
            
