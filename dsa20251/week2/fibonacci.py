# 0 1 2 3 4 5 6
# 0 1 1 2 3 5 8

def fibonacci(n):
    print(f"fibonacci({n})")
    if n==0:
        return 0
    if n==1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(6)
print(result)