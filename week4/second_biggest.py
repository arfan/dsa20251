# given an array
# find a second biggest element


def second_biggest_element(arr):
    biggest = -1
    second_biggest = -1

    for el in a:
        if el > biggest:
            second_biggest = biggest
            biggest = el
        else:
            if el > second_biggest:
                second_biggest = el
    
    return second_biggest

a = [5, 3, 2, 6]
sb = second_biggest_element(a)


print(sb)