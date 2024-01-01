#Towar od Hanoi
def hanoi(n,source,memo,target):
    if n==1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1,source,target,memo)
    print(f"Move dist {n} from {source} to {target}")
    hanoi(n-1,memo,source,target)
n=2
source_peg="A"
memo_peg="B"
target_peg="C"
hanoi(n,source_peg,memo_peg,target_peg)