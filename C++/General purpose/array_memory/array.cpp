#include <iostream>
using namespace std;

int main()
{

    int nums[5];

    cout << "Address of the nums variable: " << nums << endl;
    cout << "The same as the address of the first element nums[0]: " << &nums[0] << endl;
    cout << "The address of the second element nums[1] is right after: " << &nums[1] << endl;
    cout << "And so forth: " << &nums[2] << endl;
    return 0;
}
