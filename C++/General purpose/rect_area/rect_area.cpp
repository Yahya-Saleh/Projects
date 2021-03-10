#include <iostream>

using namespace std;

int main()
{
    int rectangles[2][3]; // length, width, area

    for (int i = 0; i < 2; i++)
    {
        // Take input for teh ith rectangle
        cout << "Enter the measurements of rectangle " << (i + 1) << ":\n";
        cout << "Length: ";
        cin >> rectangles[i][0];
        cout << "Width: ";
        cin >> rectangles[i][1];
        cout << endl;

        // Calculate the area
        rectangles[i][2] = rectangles[i][0] * rectangles[i][1];
    }

    if (rectangles[0][2] > rectangles[1][2])
    {
        cout << "Rectangle 1 has the highest area: " << rectangles[0][2] << endl;
    }
    else if (rectangles[0][2] < rectangles[1][2])
    {
        cout << "Rectangle 2 has the highest area: " << rectangles[1][2] << endl;
    }
    else
    {
        cout << "They both have the same area: " << rectangles[0][2] << endl;
    }
}