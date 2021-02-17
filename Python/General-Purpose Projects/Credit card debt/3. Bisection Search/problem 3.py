balance = 999999  # 320000
annualInterestRate = 0.18

# At best we'll pay everything with no intresent
lower_bound = balance / 12
# At worse the annual intreset will accumulate without any payments
upper_bound = (balance * (1 + annualInterestRate)) / 12

# Start in the middle
fixed_payment = (lower_bound + upper_bound) / 2

# If the fixed payment yields a debt of 0 or less
# Then we've found the lowest fixed amount to pay
debt = balance
while True:
    # Test the guess
    for _ in range(12):
        debt -= fixed_payment
        debt *= 1 + annualInterestRate / 12

    if debt > 0:
        lower_bound = fixed_payment
    elif debt < -0.5:
        upper_bound = fixed_payment
    else:
        break

    # Start in the middle
    fixed_payment = (lower_bound + upper_bound) / 2

    # Rest debt
    debt = balance


print(round(fixed_payment, 2))