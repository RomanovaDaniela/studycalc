
#!/usr/bin/env python3

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", sub(5, 2))

def abs_val(a):
    return abs(a)
# added at 2025-09-25T22:45:23.566395
# NOTE: refactor pass at 2025-09-26T15:46:03.789256

def mul(a, b):
    return a * b
# added at 2025-09-26T19:10:45.091441

def mod(a, b):
    return a % b
# added at 2025-09-26T21:04:42.461587

def div(a, b):
    if b == 0:
        return 'Error: division by zero'
    return a / b
# added at 2025-09-26T21:06:58.137287
