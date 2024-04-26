import random


def minSize():
    min = int(input("Введіть мінімальне можливе число в наборі (не менше 1) >>>>"))
    if min >= 1:
        print(f"Мінімальне число в наборі - {min}.")
    else:
        print("Невалідне число.")
        minSize()
        return min


def maxSize():
    max = int(input("Введіть максимальне можливе число в наборі (не більше 1000) >>>>"))
    if max <= 1000:
        print(f"Максимальне число в наборі - {max}.")
    else:
        print("Невалідне число.")
        maxSize()
        return max


def quantitySize():
    quantity = int(input("Введіть кількість чисел, які потрібно вибрати >>>> "))
    if quantity <= 1000:
        print(f"Кількість чисел - {quantity}.")
    else:
        print("Невалідне число.")
        quantitySize()
        return quantity
    
def create_diapazone():
    return list(range(min, max))

def get_numbers_ticket(min, max, quantity):
    create_diapazone()
    winning_numbers = random.sample(list, quantity)
    winning_numbers.sort()
    res = ', '.join(str(x) for x in winning_numbers)
    print(res)
    return res
    
get_numbers_ticket(minSize(), maxSize(), quantitySize())
 