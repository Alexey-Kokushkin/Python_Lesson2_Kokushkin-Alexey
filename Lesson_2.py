#Найти сумму чисел списка стоящих на нечетной позиции
#Пример:[1,2,3,4] -> 4

def Value():

    import random
 
    Value = random.randrange(10)  # значение от 0 до 10
    return Value

numbers=[0,0,0,0,0,0]
i=0
while i<len(numbers):
    numbers[i]=Value()
    i+=1
print(numbers)

i=0
Sum=0
while i<len(numbers):
    Sum+=numbers[i]
    i+=2
print("Сумма чисел из списка, стоящих на нечетных позициях =", Sum)