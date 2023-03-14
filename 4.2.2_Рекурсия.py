n = int(input("Размер вклада пользователя: "))
m = int(input("Срок вклада в годах: "))
c = int(input("Процентная ставка: "))
def many(n,m):
    if (m==0): return n
    many_up = n*c/100
    return many(n+many_up, m-1)
print("Размер вклада, через", m, "лет:", many(n,m))