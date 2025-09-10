def factorial(n):
    print(f"factorial({n})")
    if n==0:
        return 1
    else:
        return factorial(n-1) * n


def factorial_iter(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    
    return result

print("result is", factorial_iter(1000))
