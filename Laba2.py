import re

print("Введите количество цифр, которое натуральное число не должно превышать: ")
K = int(input())

numbers_dict = {"0": "ноль ", "1": "один ", "2": "два ", "3": "три ", "4": "четыре ", "5": "пять ", "6": "шесть ", "7": "семь ", "8": "восемь ", "9": "девять "}

check = []
file = open("test2.txt", "r")
while True:
    a = file.readline().split()
    if not a:
        print("Конец файла.")
        break
    for j in a:
        res = re.findall(r"^[1-9]*\d*[02468]$", j)
        check.append(res)


def multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str


j = 0
for i in check:
    j += 1
    if not i:
        continue
    else:
        if int(len(i[0])) <= K:
            if j % 2 == 0:
                i[0] = multiple_replace(str(i[0]), numbers_dict)
                print(i[0], "| индекс числа - ", j)
            else:
                print(i[0], "| Индекс числа - ", j)