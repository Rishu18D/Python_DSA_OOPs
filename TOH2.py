#Tower of hanai my me.....
def TOH(n,source,tempstorage,target):
    if n==1:
        print(f"move the disk 1 from {source} to {target}")
        return
    TOH(n-1,source,target,tempstorage)
    print(f"move the disk {n} from {source} to {target}")
    TOH(n-1,tempstorage,source,target)
n=3
source_peg="A"
tempstorage_peg="B"
target="C"
TOH(n,source_peg,tempstorage_peg,target)  
  