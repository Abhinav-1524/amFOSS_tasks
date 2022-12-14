n = int(input("enter n :"))
product=0
m=0
rev=0
rem=0
palindrome = []


for i in range (100 , 1000):
    for j in range (999,99,-1):
        product=i*j
        m=product
        rev=0
        while(product>0):
            rem=product%10
            rev=rev*10+rem
            product=product//10
        if(rev==m):
            if(m>100000 and m<=n):
                palindrome.append(m)

            break
        
palindrome.sort()
x=palindrome.pop()
print(palindrome)
print(x)
