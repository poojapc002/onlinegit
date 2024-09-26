def print_descending(a, b, c):
    if b > a:
        a, b = b, a
    if c > a:
        a, c = c, a
    if c > b:
        b, c = c, b
    print(a, b, c)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

print_descending(num1, num2, num3)


