temp_list = [72.5, 75.3, 71.8, 79.1, 76.0, 81.2, 77.5]

def find_highest_temp(temperatures):
    if len(temperatures) == 0:
        print("temperatures is empty")
        return

    highest_temp = temperatures[0]

    for temp in temperatures:
        if temp > highest_temp:
            highest_temp = temp
    
    return highest_temp

result = find_highest_temp(temp_list)
print(result)