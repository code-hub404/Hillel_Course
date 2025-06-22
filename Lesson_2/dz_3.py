num = int(input("Введите пятизначное число:"))
a = 10000
b = 1000
c = 100
d = 10
e = 1
left, right = divmod(num, a)
left1, right1 = divmod(right, b)
left2, right2 = divmod(right1, c)
left3, right3 = divmod(right2, d)
left4, right4 = divmod(right3, e)
left, left1, left2, left3, left4 = left4, left3, left2, left1, left
num1 = (left * 10000 + left1 * 1000 + left2 * 100 + left3 * 10 + left4 * 1)
print(num1)














