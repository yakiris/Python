#number = 43
#value = int(input('Введите число от 0 до 100 '))
#while value != number :
#    if value < number:
#        print('Нужно больше')
#    else:
#        print('Нужно меньше')
#    value = int(input('Введите число от 0 до 100 '))
#print('Вы угадали')

#1: Запросите от пользователя число, сохраните в переменную, прибавьте к числу 2 и выведите результат на экран. 

number = int(input('Введите любое число '))
print('Если к вашему числу прибавить два будет -', number + 2)

#2: Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
#После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
#Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых. И просите ввести заново.
#Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.

number = int(input('Введите число от 0 до 10 '))

while number<0 or number>10: 
    print('Неверно. Число должно быть в диапозоне от 0 до 10')
    number = int(input('Введите число от 0 до 10 '))
else:
    print('Ваше число с степени 2 равно ', number**2)   

#3: Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.
#Выведите результат согласно которому:
#Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
#Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
#Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.

name = input('Имя: ')
surname = input('Фамилия: ')
age = int(input('Возраст: '))
wage = int(input('Вес: '))

if age < 30 and 50 < wage < 120:
    print(name, surname, age, 'лет', 'вес', wage, '- хорошее состояние')
elif 30 < age < 40 and 50 > wage > 120:
    print(name, surname, age, 'лет', 'вес', wage, '- требуется занятся собой')
elif age > 40 and 50 > wage > 120:
    print(name, surname, age, 'лет', 'вес', wage, '- требуется врачебный осмотр')  
else:
    print(name, surname, age, 'лет', 'вес', wage, '- вы совершенство!')