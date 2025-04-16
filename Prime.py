X = int(input("Enter first number:"))
Y = int(input("Enter 2nd number:"))
Values = []
flag = False
if X < 2 and Y <= 2 :
   Values.append(2)
   Values.append(3)
for i in range(2, X*Y+1):
   flag = True
   for j in range(2,i):
        if i%j == 0:
            flag = False
            break
   if flag:
    Values.append(i)

print(Values)
print((Values[X-1]*Values[Y-1])-1)