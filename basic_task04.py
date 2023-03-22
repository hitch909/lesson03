# 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:

# c функцией sort()

def sum_args(arg_a, arg_b, arg_c):
    sum_val = 0
    lst = [a, b, c]
    lst.sort()
    sum_val = lst[-1] + lst[1]

    return sum_val


a = int(input("введите число a=  "))
b = int(input("введите число b=  "))
c = int(input("введите число c=  "))

print(sum_args(a, b, c))


# без функции sort()

def my_func(arg1, arg2, arg3):
    print(f'Сумма двух наибольших чисел= : {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')


my_func(
    int(input("введите число a=  ")),
    int(input("введите число b=  ")),
    int(input("введите число c=  ")),)

