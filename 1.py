n=int(input("Enter the year:"))
if (n%4)==0:
	if (n%100)==0:
		if (n%400)==0:
			print("True")
		else:
			print("False")

	else:
		print("True")

else:
	print("False")