if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]

    length = len(sample)
    target = 9

    for i in range(length):
        if sample[i] == target:
            print("found target at element", i)
            break
        
    
