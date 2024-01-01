import heapq

def find_top_k_largest(arr, k):
    # Create a min-heap with the first k elements
    min_heap = arr[:k]
    heapq.heapify(min_heap)

    # Iterate through the remaining elements in the array
    for num in arr[k:]:
        # If the current element is larger than the smallest element in the min-heap,
        # replace the smallest element with the current element
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    # The min-heap now contains the top-k largest elements
    top_k_largest = sorted(min_heap, reverse=True)
    return top_k_largest

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 3
top_k = find_top_k_largest(arr, k)
print(f"Top-{k} largest elements: {top_k}")
