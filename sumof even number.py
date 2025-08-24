A = int(input("Enter a number: "))

sum = 0

# Loop from 1 to A
for i in range(1, A + 1):
    if i % 2 == 0:
        sum += i

print("Sum of even numbers:", sum)
