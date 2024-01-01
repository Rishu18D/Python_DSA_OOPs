def combination(nums,target):
    result=[]
    nums.sort()
    def backtrack(remain,path,start):
        if remain==0:
            result.append(path)
            return
        for i in range(start,len(nums)):
            if nums[i]>remain:
                break
            backtrack(remain-nums[i],path+[nums[i]],i)
    backtrack(target,[],0)
    return result
nums=[2,3,6,7]
target=7
result=combination(nums,target)
print(f"The combination of the {target} is: {result}")
            

