a=int(input("Введи число"))
b=(a%10)
c=((a//10)%10) 
if b>c:
 print(b)
 print(c)
elif c>b:
 print(c)
 print(b)
else:
     print("Вони однакові")