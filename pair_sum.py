def pair_sum(nums,target):
    n=len(nums)
    result=[]
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                result.append([nums[i],nums[j]])
                return result
nums=[1,2,3,4,5]
target=5
result=pair_sum(nums,target)
if result:
    print(f"The pairs that sum upto the target are:{result}")
else:
    print("No such pair found")