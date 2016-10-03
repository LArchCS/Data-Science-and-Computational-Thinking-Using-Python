epsilon = 0.000001
x = 9.06
a = x/2.0
y=a**(0.5)

while abs(y - x**(0.5)) >= epsilon:
    print(y)
    a=y**2
    slope=(0.5)*(a**(-0.5))
    y = y+((x-a)*slope)

print('Square root of ' + str(x) + ' is about ' + str(y))