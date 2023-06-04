# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. 
# Разрешается использовать только операцию умножения. 
# Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def Pow(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * Pow(a, b - 1))
a = int(input("Input A "))
b = int(input("Input B "))
print(Pow(a, b))
        