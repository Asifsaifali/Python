# Code for reverse || Palindrom || Sum of digits

n = int(input("Enter the number:"))
num = n
rev = 0
sum = 0
while n!=0:
    rem = n%10
    rev = rev * 10 + rem
    n //= 10
    sum += rem
if num == rev:
   print("Palindrom")
else:
    print("Not palindrom")

print("Sum of digits is:",sum)
