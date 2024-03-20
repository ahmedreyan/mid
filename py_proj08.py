def tower_of_hanoi(disks, source, auxiliary, target):
    if disks == 1:
        print("Move disk 1 from rod {}".format(source, target))
        return
    tower_of_hanoi(disks-1, source, target, auxiliary)
    print("Move disks {} from rod {}".format(disks, source, target)) 
    tower_of_hanoi(disks-1, auxiliary, source, target)
disks = int(input("Enter the Number of disk: "))
tower_of_hanoi(disks, "A", "B", "C")