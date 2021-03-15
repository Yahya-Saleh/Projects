/*
Write a function countEven int *, int ) which receives an integer array and its size, and returns
the number of even numbers in the array.
*/
#include <iostream>
using namespace std;

int countEven(int *array, int size);

int main()
{
    int SIZE = 5;
    int nums[SIZE];

    for (int i = 0; i < SIZE; i++)
    {
        cout << "Enter number #" << i + 1 << ": ";
        cin >> nums[i];
    }

    cout << "You have entered " << countEven(nums, SIZE) << " even number(s)";
}

int countEven(int *array, int size)
{
    int even = 0;
    for (int i = 0; i < size; i++)
    {
        if (array[i] % 2 == 0)
        {
            even++;
        }
    }

    return even;
}
