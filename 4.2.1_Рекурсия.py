n = int(input("Размер вклада пользователя: "))
m = int(input("Срок вклада в годах: "))
def many(n,m):
    return 0 if m == 0 else n+many(n, m-1)
print("Размер вклада, через", m, "лет:", many(n, m))