#include <iostream>

using namespace std;

int main()
{
    float m, cm, inch;
    int ft;

    cout << "Enter a value in meters to be converted: ";
    cin >> m;

    cm = m * 100;
    inch = cm / 2.54;
    ft = (int)inch / 12;
    inch = (int)inch % 12;

    cout << cm << "cm = " << ft << "ft and " << inch << "in\n";
}