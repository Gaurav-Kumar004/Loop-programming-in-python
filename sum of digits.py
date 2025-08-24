num=int(input("Enter the number"))
Sum=0
while num>0:
    digits=num % 10
    Sum=Sum+digits
    num=num//10
print("sum of digits",Sum)
