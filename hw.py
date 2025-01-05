from math import sqrt


message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_sqareroot(number):
    """Вычисляет квадратный корень.
    """
    return sqrt(number)


def calc(your_number):
    """Полуачет на вход число,
    возвращает на экран его квадратный корень.
    """
    if your_number <= 0:
        return
    res = calculate_sqareroot(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {res}')


print(message)
calc(25.5)
