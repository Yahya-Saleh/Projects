# Credit card debt

A three part project implementing programs that answer questions pertaining to credit card debt

## Background

Each month, a credit card statement will come with the option for you to pay a minimum amount of your charge, usually 2% of the balance due. However, the credit card company earns money by charging interest on the balance that you don't pay. So even if you pay credit card payments on time, interest is still accruing on the outstanding balance.

Say you've made a $5,000 purchase on a credit card with an 18% annual interest rate and a 2% minimum monthly payment rate. If you only pay the minimum monthly amount for a year, how much is the remaining balance?

You can think about this in the following way.

At the beginning of month 0 (when the credit card statement arrives), assume you owe an amount we will call  b0  (b for balance; subscript 0 to indicate this is the balance at month 0).

Any payment you make during that month is deducted from the balance. Let's call the payment you make in month 0,  ${p}_{0}$ . Thus, your unpaid balance for month 0,  ub0 , is equal to  ${b}_{0}−{p}_{0}$ .

> ${ub}_{0} = {b}_{0} − {p}_{0}$

At the beginning of month 1, the credit card company will charge you interest on your unpaid balance. So if your annual interest rate is  r , then at the beginning of month 1, your new balance is your previous unpaid balance  ${ub}_{0}$ , plus the interest on this unpaid balance for the month. In algebra, this new balance would be

> ${b}_{1} = {ub}_{0} + \frac{r}{12.0} * {ub}_{0}$

In month 1, we will make another payment,  ${p}_{1}$ . That payment has to cover some of the interest costs, so it does not completely go towards paying off the original charge. The balance at the beginning of month 2,  ${b}_{2}$ , can be calculated by first calculating the unpaid balance after paying  ${p}_{1}$ , then by adding the interest accrued:

> ${ub}_{1}={b}_{1} − {p}_{1}$

> ${b}_{2}={ub}_{1}+\frac{r}{12.0} * {ub}_{1}$

If you choose just to pay off the minimum monthly payment each month, you will see that the compound interest will dramatically reduce your ability to lower your debt.
