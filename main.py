n=int(input('Enter a number:'))
sum=0
temp=n
length=len(str(n))
while temp>0:
 digit=temp%10
 sum=sum+digit**length
 temp=temp//10
 print("The Total Digits are:",sum)