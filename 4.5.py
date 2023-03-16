list_of_numbers = input('введите список чисел: ').split(' ')
a = 1
for i in range(1, len(list_of_numbers)):
    if list_of_numbers[i - 1] != list_of_numbers[i]:
        a += 1
print(a)

