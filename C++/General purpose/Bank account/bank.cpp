#include <iostream>
using namespace std;

class BankAccount
{
private:
    double balance;
    // % wise
    double interest_rate = 0;

public:
    BankAccount(int dollars, int cents)
    {
        set(dollars, cents);
    }

    // The account balance is set to $dollars.cents
    void set(int dollars, int cents)
    {
        balance = dollars + (cents / 100.0);
    }
    // One year of simple interest is added to account balance
    void update()
    {
        balance += balance * (interest_rate / 100.0);
    }
    // Return the current account balance
    double get_balance()
    {
        return balance;
    }
    // Return the current interest rate
    double get_rate()
    {
        return interest_rate;
    }
    // Rate is set to interest rate
    void set_rate(int rate)
    {
        interest_rate = rate;
    }
};

int main()
{
    BankAccount account = BankAccount(2000, 75);

    cout << account.get_balance() << endl;

    cout << account.get_rate() << endl;
    account.set_rate(10);
    cout << account.get_rate() << endl;

    account.update();
    cout << account.get_balance() << endl;
}