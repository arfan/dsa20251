if __name__ == "__main__":
    sample = [1, 2, 5, 6, 9]

    length = len(sample)
    target = 3

    for i in range(length):
        print("current element=", sample[i])
        if sample[i] == target:
            print("found target at element", i)
            break
        elif sample[i] > target:
            print("current element is bigger, stop early")
            break 
    
