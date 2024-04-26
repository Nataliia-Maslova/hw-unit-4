import random

def get_numbers_ticket(min, max, quantity):

    diapazone = list(range(min, max))

    winning_numbers = random.sample(diapazone, quantity)
    winning_numbers.sort()
    res = ', '.join(str(x) for x in winning_numbers)
    print(res)
    return res


min = int(input("Введіть мінімальне можливе число в наборі (не менше 1) >>>> ")) 
max = int(input("Введіть максимальне можливе число в наборі (не більше 1000) >>>> ")) 
quantity = int(input("Введіть кількість чисел, які потрібно вибрати >>>> "))

get_numbers_ticket(min, max, quantity)

