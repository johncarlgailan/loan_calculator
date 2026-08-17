loan_amount = float(input("Enter loan amount: "))
months_pay = int(input("Enter amount of months to pay: "))
interest_rate = 0.10

monthly_interest = (loan_amount * interest_rate)
total_interest = (monthly_interest * months_pay)
total_loan = (loan_amount + total_interest)
monthly_payment = (total_loan / months_pay)

print("Loan amount:", loan_amount)
print("Interest rate:", "10%")
print("Monthly interest:", monthly_interest)
print("Total interest:", total_interest)
print("Total loan:", total_loan)
print("Monthly payment:", monthly_payment)