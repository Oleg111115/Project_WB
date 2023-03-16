list_of_numbers = input('введите список чисел: ').split(' ')
a = 0
for i in range(1, len(list_of_numbers)-1):
    if list_of_numbers[i-1] < list_of_numbers[i] > list_of_numbers[i+1]:
        a += 1
print(a)
