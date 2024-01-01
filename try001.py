#Combination Sum....
def abc(nums,target):
    result=[]
    nums.sort()
    def backtrack(remain,path,start):
        if remain==0:
            result.append(path)
            return
        for i in range(start, len(nums)):
            if nums[i] > remain:
                break
            backtrack(remain - nums[i], path + [nums[i]], i)

    backtrack(target, [], 0)
    return result

# Example usage:
candidates = [2, 3, 6, 7]
target = 7
result = abc(candidates, target)
print(f"The combinations that sum up to {target} are: {result}")
             