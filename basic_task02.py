# 2. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль (try except).

def div_numbers(number, next_namber):
    result = number / next_namber
    return result


try:
    number = int(input("Укажите первое число: "))
    next_number = int(input("Укажите второе число: "))
    if number == 0 or next_number == 0:
        print("Вы что? Пытаетесь делить на 0!")
        print("Process finished with exit code 0")
except ValueError:
    print("Process finished with exit code 0")

else:
    print(div_numbers(number, next_number))

