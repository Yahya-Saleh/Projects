/*
Write a program that asks the user two positive integer values. The
program should use a loop to get the sum of all the integers from the first up
to the second number entered. For example, if the user enters 50, the loop
will find the sum of 1, 2, 3, 4, … 50.

Input validation: Do not accept a negative number.
*/

#include <iostream>

using namespace std;

int main()
{
    int nums[2];
    for (int i = 0; i < 2; i++)
    {
        do
        {
            cout << "Enter a positive number " << i + 1 << ": ";
            cin >> nums[i];

        } while (nums[i] < 1);
    }

    int total = 0;
    for (int i = nums[0]; i <= nums[1]; i++)
    {
        total += i;
    }

    cout << "Total from " << nums[0] << " to " << nums[1] << ": " << total;
}