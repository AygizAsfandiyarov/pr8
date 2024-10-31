def kvadrat(size):
    for i in range(size):
        for j in range(size):
            # Условие для отрисовки границы
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()  # Переход на новую строку

# Размер квадрата
size = 10
kvadrat(size)