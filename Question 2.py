def mod_exp(x, b, n):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * x) % n
        x = (x * x) % n
        b //= 2
    return result

x = int(input("Enter x: "))
b = int(input("Enter b: "))
n = int(input("Enter n: "))

print("Result: ", mod_exp(x, b, n))