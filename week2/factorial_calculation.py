def factorial(n):
    print(f"factorial({n})")
    if n==0:
        return 1
    else:
        return factorial(n-1) * n

print("result is", factorial(5))
