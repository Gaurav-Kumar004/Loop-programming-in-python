n=int(input("Enter a number:"))
rev=0
m=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if rev==m :
    print('Palindrome')
else:
    print('Not a palindrome')