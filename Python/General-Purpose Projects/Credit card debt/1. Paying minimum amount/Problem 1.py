balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# For each month
for _ in range(12):
    # Minimum amount to be paid
    paid_amount = balance * monthlyPaymentRate
    # Assume that minimum amount is paid
    balance -= paid_amount
    # Add monthly intreset to the paid remaining debt
    balance *= 1 + annualInterestRate / 12

print("Remaining balance:", round(balance, 2))