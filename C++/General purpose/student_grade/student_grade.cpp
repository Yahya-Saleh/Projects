/*
A student’s mark for a module is calculated based on 20% quiz, 30% assignment and 50%
final exam.

Write a C++ program for a teacher to enter and calculate the marks of his/her students in a
class. The program should ask the teacher the number of students in the class and
appropriately create array of that size to store the mark.
Then, determine the average mark for students in the class.

Input validation: Marks for each component should not be more than the maximum allocated
mark.
*/

#include <string>
#include <iostream>
using namespace std;

double get_avg(double *array, int size);
void populate_stud_grades(double *stud_grades, int size);

int main()
{
    // Get the number of students
    int students;
    cout << "Enter the number of students: ";
    cin >> students;

    // Create an array of size students initiated with a grade of 0
    double *stud_grades = new double[students]{0};

    populate_stud_grades(stud_grades, students);

    cout << "The average grade in this class is " << get_avg(stud_grades, students);

    delete stud_grades;
}

void populate_stud_grades(double *stud_grades, int size)
{
    // To temperary hold inputted grade
    double buffer;
    for (int i = 0; i < size; i++)
    {
        cout << "Enter grades for student " << i + 1 << endl;

        // category name and its highest grade
        string display[3][2] = {{"Quiz", "20"}, {"Assignment", "30"}, {"Final exam", "50"}};
        // Keep looping until the student's grade is entered correctly
        int j = 0;
        while (j < 3)
        {
            // Get the grade
            cout << "   " << display[j][0] << " grade (out of " << display[j][1] << "): ";
            cin >> buffer;
            // If the input is correct go on to the next category
            if (0 <= buffer && buffer <= stoi(display[j][1]))
            {
                stud_grades[i] += buffer;
                j++;
            }
            // Otherwise stay on the same category and display an error message
            else
            {
                cout << "   Enter a grade within range!" << endl;
            }
        }
    }
}

double get_avg(double array[], int size)
{
    double total = 0;
    for (int i = 0; i < size; i++)
    {
        total += array[i];
    }

    return total / size;
}