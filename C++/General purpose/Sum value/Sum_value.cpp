/*
Write a program that asks the user for a positive integer value. The
program should use a loop to get the sum of all the integers from 1 up
to the number entered. For example, if the user enters 50, the loop
will find the sum of 1, 2, 3, 4, … 50.

Input validation: Do not accept a negative number.
*/

#include <iostream>

using namespace std;

int main()
{
    int num;
    do
    {
        cout << "Enter a positive number: ";
        cin >> num;

    } while (num < 1);

    int total = 0;
    for (int i = 1; i <= num; i++)
    {
        total += i;
    }

    cout << "Total from 1 to " << num << " : " << total;
}