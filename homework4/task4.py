
def get_integer(number):
    while True:
        try:
            return int(input(number))
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")

# Запрос ввода чисел a и b
a = get_integer("Введите первое число (a): ")
b = get_integer("Введите второе число (b): ")

# Вывод всех целых чисел между a и b
if a < b and (b - a) > 1:
    for i in range(a + 1, b):
        print(i)
elif a > b and (a - b) > 1:
    for i in range(b + 1, a):
        print(i)
else:
    print(" Нет целых чисел между ними.")