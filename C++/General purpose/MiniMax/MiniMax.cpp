#include <iostream>
using namespace std;

int main()
{
    // array size
    int num_size = 10;
    int nums[num_size];

    // Get nums
    for (int i = 0; i < num_size; i++)
    {
        cout << "Enter num #" << i + 1 << ": ";
        cin >> nums[i];
    }

    // Evaluate the min and max
    int min = nums[0];
    int max = nums[0];
    for (int i = 1; i < num_size; i++)
    {
        if (nums[i] < min)
        {
            min = nums[i];
        }
        else if (nums[i] > max)
        {
            max = nums[i];
        }
    }

    cout << "Biggest number: " << max << endl;
    cout << "Smallest number: " << min << endl;
}