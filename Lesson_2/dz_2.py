num = int(input("Введите целое число:"))
a = 1000
digit = num
left, right = divmod(digit, a)
print(left)

b = 100
digit1 = right
left1, right1 = divmod(digit1, b)
print(left1)

c = 10
digit2 = right1
left2, right2 =divmod(digit2, c)
print(left2)

d = 1
digit3 = right2
left3,right3 =divmod(digit3, d)
print(left3)













