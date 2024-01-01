#Backtracking...
def C_sum(candidates, target):
    res = []
    candidates.sort()

    def backtrack(remain, path, start):
        if remain == 0:
            res.append(path)
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                break
            backtrack(remain - candidates[i], path + [candidates[i]], i)

    backtrack(target, [], 0)
    return res

# Example usage:
candidates = [2, 3, 6, 7]
target = 7
result = C_sum(candidates, target)
print(f"The combinations that sum up to {target} are: {result}")
