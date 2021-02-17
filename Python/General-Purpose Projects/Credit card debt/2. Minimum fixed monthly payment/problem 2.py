import math

balance = 4773
annualInterestRate = 0.2

# Start with a guess
fixed_payment = balance / 12
# Round up to the 10 as per the specification
fixed_payment = int(math.ceil(fixed_payment / 10)) * 10

# Decrement to fix for the first increment in the loop
fixed_payment -= 10
# If the fixed payment yields a debt of 0 or less
# Then we've found the lowest fixed amount to pay
debt = balance
while debt > 0:
    # Increase fixed_payment by 10 since the
    # specification requires a multiple of 10
    fixed_payment += 10
    # Rest/create debt
    debt = balance
    # Test the guess
    for _ in range(12):
        debt -= fixed_payment
        debt *= 1 + annualInterestRate / 12


print(fixed_payment)