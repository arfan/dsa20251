def tower_of_hanoi(n, source, auxilary, destination):
    if n==1:
        print("Move disk 1 from", source, "to", destination)
        return
    else:
        tower_of_hanoi(n-1, source, destination, auxilary)
        print("Move disk", n, "from", source, "to", destination)
        tower_of_hanoi(n-1, auxilary, source, destination)

tower_of_hanoi(3, "A", "B", "C")
