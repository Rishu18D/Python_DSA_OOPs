def abc_dp(nums, target):
    nums.sort()
    dp = {}
    
    def backtrack(remain, start):
        if remain == 0:
            return [[]]
        if (remain, start) in dp:
            return dp[(remain, start)]
        
        result = []
        for i in range(start, len(nums)):
            if nums[i] > remain:
                break
            subproblems = backtrack(remain - nums[i], i)
            for path in subproblems:
                result.append([nums[i]] + path)
        
        dp[(remain, start)] = result
        return result
    
    return backtrack(target, 0)

nums = [3, 4, 2, 5, 3, 7, 6, 5, 4, 8, 7, 8, 9]
target = 100
result = abc_dp(nums, target)
print(result)
