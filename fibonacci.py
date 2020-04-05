n=int(input('enter the number'))
i=0
n1=0
n2=1
while(i<n):
    if(i<=1):
        sum=i
    else:
        sum=n1+n2
        n1=n2
        n2=sum
    print(sum)
    i+=1
