/*
Write a program that asks the user to enter a number within the
range of 1 through 10. Use a switch statement to display the Roman
numeral version of that number.

Input validation: Do not accept a number less than 1 or greater than
10. 
*/

#include <iostream>
using namespace std;

int main()
{
    int num;
    do
    {
        cout << "Enter a number between 1-10 (inclusive): ";
        cin >> num;

    } while (1 > num || num > 10);

    switch (num)
    {
    case 1 ... 3:
        for (int i; i < num; i++)
        {
            cout << "I";
        }
        break;

    case 4:
        cout << "IV";
        break;

    case 5 ... 8:
        cout << "V";
        for (int i; i < num - 5; i++)
        {
            cout << "I";
        }
        break;

    case 9:
        cout << "IX";
        break;
    case 10:
        cout << "X";
        break;
    }
}
