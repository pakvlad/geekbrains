a = int(input('введите целое положительное число:'))
b = 0
res = 0
while a>0:
    b = a%10
    if res<b:
        res = b
    a=a//10
print(res)