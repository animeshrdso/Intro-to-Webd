print("Enter the number")
n=int(input())
num1=0
num2=1
print("The fibonacci series is")
sum=0
print(sum)
for i in range(1,n):
	if i==1:
		print(i)
	else:
		sum=num1+num2
		num1=num2
		num2=sum
		print(sum)