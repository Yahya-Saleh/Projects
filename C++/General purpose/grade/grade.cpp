#include <iostream>
#include <string>
using namespace std;

int main()
{
    string correct_ans[15] = {"a",
                              "c",
                              "b",
                              "b",
                              "d",
                              "d",
                              "c",
                              "a",
                              "b",
                              "a",
                              "a",
                              "a",
                              "c",
                              "d",
                              "c"};

    string ans[15];
    int score = 0;
    // Get the answer and grade it at teh same time
    for (int i = 0; i < 15; i++)
    {
        cout << "Question #" << i + 1 << " answer: ";
        cin >> ans[i];

        if (ans[i] == correct_ans[i])
        {
            score++;
        }
    }

    // Evaluate the grade
    if (score >= 12)
    {
        cout << "You pass!";
    }
    else
    {
        cout << "You failed!";
    }
    cout << " with a score of " << score << "/15" << endl;
}