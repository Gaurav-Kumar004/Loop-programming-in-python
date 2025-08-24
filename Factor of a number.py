# num = int(input("Enter a number: "))

# print(f"Factors of {num} are:")

# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i) 

n=int(input("Enter the number:-   "))
i=1
while(i<=n):
    if(n%i==0):
        print(i)
    i+=1
