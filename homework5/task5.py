sum = 0

while True:
    user_input = input("Введите число (или 'stop'/'end' для завершения): ")
    
    if user_input.lower() in ["stop", "end"]:
        break
    
    try:
        number = float(user_input)
        sum += number
    except ValueError:
        print("Ошибка: пожалуйста, введите корректное число.")
        continue

print("Сумма введенных чисел:", sum)