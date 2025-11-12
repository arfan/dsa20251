for A in range(0, 10):
    for B in range(0, 10):
        num1 = int(f"{B}{A}{A}{A}")
        num2 = int(f"{B}{B}{B}{A}")
        num3 = int(f"{A}{A}{A}{B}")

        if num1+num2==num3:
            print(num1, num2, num3)