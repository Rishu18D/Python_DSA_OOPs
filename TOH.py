def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, source, target)

# Example usage:
n = 3  # Replace with the number of disks you want to move
source_peg = "A"  # Replace with the source peg's name
auxiliary_peg = "B"  # Replace with the auxiliary peg's name
target_peg = "C"  # Replace with the target peg's name

hanoi(n, source_peg, auxiliary_peg, target_peg)
