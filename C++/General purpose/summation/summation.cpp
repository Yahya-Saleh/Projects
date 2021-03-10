#include <iostream>
using namespace std;

int main()
{
    int num_size = 10;
    int nums[num_size];

    for (int i = 0; i < num_size; i++)
    {
        cout << "Enter num #" << i + 1 << ": ";
        cin >> nums[i];
    }

    int total = 0;
    for (int i = 0; i < num_size; i++)
        total += nums[i];

    cout << "Total: " << total << endl;
}