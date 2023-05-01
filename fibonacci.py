def fibonacci(num):
    if num == 1 or num == 0:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(100))
