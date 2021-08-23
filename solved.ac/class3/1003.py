def fibonacci(num):
    if num == 0:
        print("0")
        return 0
    elif num == 1:
        print("1")
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

x = fibonacci(3)
print(x)