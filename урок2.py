user_number = input ("Введите 4-х значное число: ")
dig_1, remainder = divmod(int(user_number), 1000)
dig_2, remainder = divmod(remainder, 100)
dig_3, dig_4 = divmod (remainder, 10)
print(dig_1)
print (dig_2)
print (dig_3)
print (dig_4)


n1 = int(input("Введите целое число: "))

digit = n1 % 10
n2 = digit
n1 = n1 // 103
while n1 > 0:
    digit = n1 % 10

    n1 = n1 // 10

    n2 = n2 * 10

    n2 = n2 + digit
print("Результат:", n2)