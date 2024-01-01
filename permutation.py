def permute(nums):
    def backtrack(start):
        if start == len(nums) - 1:
            result.append(nums[:])  # Make a copy of the current permutation
            return

        for i in range(start, len(nums)):
            # Swap the current element with the element at index 'start'
            nums[start], nums[i] = nums[i], nums[start]

            # Recursively generate permutations for the remaining elements
            backtrack(start + 1)

            # Undo the swap (backtrack)
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack(0)
    return result

# Example usage:
input_list = [1, 2, 3]
permutations = permute(input_list)
print("Permutations:", permutations)
