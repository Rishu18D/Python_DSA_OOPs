#Write Knapsack 0/1 problem using brute force method..
def kanpsack(W,wt,val,n):
    if W==0 or n==0:
        return 0
    elif (wt[n-1]>W):
        return kanpsack(W,wt,val,n-1)
    else:
        return max(val[n-1] + kanpsack(W-wt[n-1],wt,val,n-1),kanpsack(W,wt,val,n-1))
val=[60,100,120]
wt=[10,20,30]
W=50
n=len(val)
print(kanpsack(W,wt,val,n))    
    