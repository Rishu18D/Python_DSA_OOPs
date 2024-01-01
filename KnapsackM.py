#Using dynamic programming (Memoization method) write code for KNAPSACK 0/1 problem...
def knapsack(W,wt,val,n,memo={}):
    if W==0 or n==0:
        return 0
    elif (n,W) in memo:
        return memo[(n,W)]
    elif wt[n-1]>W:
        memo[(n,W)]=knapsack(W,wt,val,n-1,memo)
        return memo[(n,W)]
    else:
        memo[(n,W)]=max(val[n-1] + knapsack(W-wt[n-1],wt,val,n-1,memo),knapsack(W,wt,val,n-1,memo))
        return memo[(n,W)]
val=[60,100,120]
wt=[10,20,30]
W=50
n=len(val)
result=knapsack(W,wt,val,n,)
print("The higest value can be in the knapsack is:",result)    