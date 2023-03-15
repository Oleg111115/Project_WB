print("Введите два числа и знак +, -, *, /")
n = int(input())
m = int(input())
c = input()
def calculator(n,m,c):
    if c == "*":
        return n*m
    elif c == "/":
        return n/m
    elif c == "+":
        return n+m
    elif c == "-":
        return n-m
print(calculator(n, m, c))
