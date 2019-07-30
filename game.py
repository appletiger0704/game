import random 
x = random.randint(1,10)
while True :
 i = input('猜一個數字')
 i = int(i)

 if  i == x :
    print('猜對了')
    break
 else :
    print('猜錯囉')
    if i > x :
        print('比答案大')
    elif i < x :
        print('比答案小')
