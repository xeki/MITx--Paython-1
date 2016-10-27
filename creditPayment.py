def creditPayment(b,ai,mr):
	b = b/1.0
	annualInterestRate = ai
	monthlyPaymentRate = mr
	monthlyInterestRate = ai / 12.0
	for i in range(12):
		minimumMonthlyPayment = monthlyPaymentRate*b
		b = b - minimumMonthlyPayment
		b = b + b*monthlyInterestRate
		print ("Remaining Balance: "+ str(i) + " " + str(round(b,2)))
	return b
def fixedMonthlyPayment(b,ai,mp):
	b = b/1.0
	annualInterestRate = ai
	monthlyPayment = mp
	monthlyInterestRate = ai / 12.0
	for i in range(12):
		b = b - monthlyPayment
		b = b + b*monthlyInterestRate
		#print ("Remaining Balance: " + str(i) + " " + str(round(b,2)))
	return b	
def findMinimumFixedPayment(b,ai):
	lb = b/12.0
	ub = (b*((1.0+ai/12.0)**12)/12.0)
	mp = (lb + ub)/2.0
	rb = fixedMonthlyPayment(b,ai,mp)
	while rb!=0:
		if rb  > 0:
			lb = mp 
			mp = (lb + ub)/2.0
		elif rb < 0:
			ub = mp
			mp = (lb + ub)/2.0
		rb = fixedMonthlyPayment(b,ai,mp)
	print("Minimum Fixed Payment : " + str(round(mp,2)))
	
b = 42
ai = 0.2
mr = 0.04

creditPayment(b,ai,mr)
findMinimumFixedPayment(320000,0.2)
findMinimumFixedPayment(999999,0.18)
