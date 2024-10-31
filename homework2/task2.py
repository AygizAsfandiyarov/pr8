while True:
    # Ввод целых чисел
    try:
        number1 = int(input("Введите первое целое число:"))
        number2 = int(input("Введите второе целое число:"))

        #Вывод суммы двух целых чисел
        print("Сумма равна", number1 + number2)
    except ValueError:
        print("Ошибка. Введите целое число")
