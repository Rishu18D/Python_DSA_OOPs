def subset_sum(nums, target):
    def backtrack(start, path, curr_sum):
        if curr_sum == target:
            result.append(path[:])
            return
        for i in range(start, len(nums)):
            if curr_sum + nums[i] <= target:
                path.append(nums[i])
                backtrack(i + 1, path, curr_sum + nums[i])
                path.pop()

    result = []
    nums.sort()  # optional, for optimized output
    backtrack(0, [], 0)
    return result
nums = [1, 2, 3, 4, 5]
target = 7
subsets = subset_sum(nums, target)
print(subsets)
