#Найти сумму чисел списка стоящих на нечетной позиции
#Пример:[1,2,3,4] -> 4

#def Value():

    #import random
 
    #Value = random.randrange(10)  # значение от 0 до 10
    #return Value

#numbers=[0,0,0,0,0,0]
#i=0
#while i<len(numbers):
    #numbers[i]=Value()
    #i+=1
#print(numbers)

#i=0
#Sum=0
#while i<len(numbers):
    #Sum+=numbers[i]
    #i+=2
#print("Сумма чисел из списка, стоящих на нечетных позициях =", Sum)


# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

#from operator import le


#def Value():

    #import random
 
    #Value = random.randrange(10)  # значение от 0 до 10
    #return Value

#numbers=[0,0,0,0,0,0]
#i=0
#while i<len(numbers):
    #numbers[i]=Value()
    #i+=1
#print(numbers)

#i=0
#Multiplication=0
#while i<len(numbers)/2:
    #Multiplication=numbers[i]*numbers[len(numbers)-i-1]
    #i+=1
    #print(Multiplication)


# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers=[1.1, 1.2, 3.1, 5.02, 10.01]
NewNumbers=[0.0,0.0,0.0,0.0,0.0]
j=int(0)
while j<=len(numbers)-1:
    NewNumbers[j]=round(numbers[j]%1, 2)
    j+=1
print(NewNumbers)

min=NewNumbers[0]
i=0
while i<=len(NewNumbers)-1:
    if NewNumbers[i]<min:
        min=NewNumbers[i]
    i+=1
print("Минимальное значение дробной части =",min)

max=NewNumbers[0]
i=0
while i<=len(NewNumbers)-1:
    if NewNumbers[i]>max:
        max=NewNumbers[i]
    i+=1
print("Максимальное значение дробной части =",max)

dif=max-min
print("Разница между максимальным и минимальным значением дробной части элементов =",dif)


#number = numbers[4]%1
#print(round(number,2))

