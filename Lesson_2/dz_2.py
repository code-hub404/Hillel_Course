from prompt_toolkit.shortcuts import clear

num = int(input("Введите целое число:"))
a = 1000
digit = num
left, right = divmod(digit, a)
b = 100
digit1 = right
left1, right1 = divmod(digit1, b)
c = 10
digit2 = right1
left2, right2 =divmod(digit2, c)
d = 1
digit3 = right2
left3,right3 =divmod(digit3, d)
print(left)
print(left1)
print(left2)
print(left3)













