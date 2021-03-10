#include <iostream>
using namespace std;

void swap(int &x, int &y);
void bubble_sort(int nums[], int size);

int main()
{
    int num_size = 10;
    int *nums = new int[num_size];
    for (int i = 0; i < num_size; i++)
    {
        cout << "Enter num " << i + 1 << ": ";
        cin >> nums[i];
    }

    bubble_sort(nums, num_size);

    cout << "sorted array: { ";
    for (int i = 0; i < num_size; i++)
        cout << nums[i] << " ";

    cout << "}" << endl;

    delete[] nums;
}

void swap(int &x, int &y)
{
    int z = x;
    x = y;
    y = z;
}

void bubble_sort(int nums[], int size)
{
    // Repeat a number of times equal to the array's size
    for (int j = 0; j < size; j++)
    {
        bool swapped = false;
        // Put the biggest element at the end of the list
        for (int i = 0; i < size - j - 1; i++)
        {
            if (nums[i] > nums[i + 1])
            {
                swap(nums[i], nums[i + 1]);
                swapped = true;
            }
        }

        if (!swapped)
        {
            break;
        }
    }
}