def subset_sum(nums, target):
    nums.sort()
    dp = [0] * (target + 1)
    dp[0] = 1

    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] += dp[i - num]

    result = []
    if dp[target] > 0:
        # Reconstruct the subset
        stack = [(target, [])]
        while stack:
            current_target, current_subset = stack.pop()
            for i, num in enumerate(nums):
                if num <= current_target and dp[current_target - num] > 0:
                    stack.append((current_target - num, current_subset + [num]))

            if current_target == 0:
                result.append(current_subset)

    return result

nums = [3, 4, 2, 5, 3, 7, 6, 5, 4, 8, 7, 8, 9]
target = 50
result = subset_sum(nums, target)
print(result)
