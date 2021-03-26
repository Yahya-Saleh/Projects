#include <iostream>
#include <string>
#include <sstream>
#include <conio.h>

using namespace std;

struct student
{
    int stud_id;
    int test, assignment,
        quiz, final;
    student *next = NULL;
};

class class_room
{
    student *head = NULL;
    int size = 0;
    int id = 0;

    int work_size = 4;
    string work[4][2] = {{"Midterm-test", "20"}, {"Quiz", "10"}, {"Assignment", "20"}, {"Final exam", "50"}};

public:
    class_room()
    {
        menu();
    }
    void menu()
    {
        int option;
        while (true)
        {
            cout << "Welcome to class CLI:\n\t1. Add new records\n\t2. Add a record\n\t3. Display records\n\t4. Get best student\n\n\t0. Exit\n";
            cout << "\nPick an option: ";
            cin >> option;

            if (option == 1)
            {
                int records;
                cout << "How many records fo you wish to: ";
                cin >> records;
                new_records(records);
            }
            else if (option == 2)
                new_record();
            else if (option == 3)
                display_records();
            else if (option == 4)
                best_student();
            else if (option == 0)
                break;
            else
                cout << "\nPick a valid option\n"
                     << endl;

            cout << "\nPress any key to continue...\n";
            getch();
        }
    }
    void new_records(int n)
    {
        for (int i = 1; i < n + 1; i++)
        {
            cout << "Enter the information for student " << i << "\n\n";
            new_record();
            cout << "\n\n";
        }
    }
    void new_record()
    {
        student *stud = new student;
        int grade;
        // Prompt for every work
        int i = 0;
        while (i < 4)
        {
            cout << "Enter the " << work[i][0] << " grade (out of " << work[i][1] << "): ";
            cin >> grade;
            if (0 > grade || grade > stoi(work[i][1]))
                cout << "Please enter a grade within range!" << endl;
            else
            {
                if (work[i][0] == "Midterm-test")
                    stud->test = grade;
                else if (work[i][0] == "Quiz")
                    stud->quiz = grade;
                else if (work[i][0] == "Assignment")
                    stud->assignment = grade;
                else if (work[i][0] == "Final exam")
                    stud->final = grade;

                i++;
            }
        }
        stud->stud_id = id++;
        append_student(stud);
    }
    void append_student(student *stud)
    {
        if (head == NULL)
            head = stud;
        else
        {
            student *last = head;
            for (; last->next != NULL; last = last->next)
            {
            }
            last->next = stud;
            stud->next = NULL;
        }
    }

    void display_records()
    {
        if (head == NULL)
        {
            cout << "\nNo records stored\n"
                 << endl;
            return;
        }
        for (student *trv = head; trv != NULL; trv = trv->next)
        {
            cout << "\tID: " << trv->stud_id;
            cout << "\tMidterm-test: " << trv->test;
            cout << "\tQuiz: " << trv->quiz;
            cout << "\tAssignment: " << trv->assignment;
            cout << "\tFinal exam: " << trv->final << endl;
        }
    }

    void best_student()
    {
        if (head == NULL)
        {
            cout << "\nNo records stored\n"
                 << endl;
            return;
        }

        student *best = head;
        int best_total = best->test + best->quiz + best->assignment + best->final;
        int total;
        for (student *trv = head->next; trv != NULL; trv = trv->next)
        {
            total = trv->test + trv->quiz + trv->assignment + trv->final;
            if (total > best_total)
            {
                best = trv;
                best_total = total;
            }
        }

        cout << "\tID: " << best->stud_id;
        cout << "\tMidterm-test: " << best->test;
        cout << "\tQuiz: " << best->quiz;
        cout << "\tAssignment: " << best->assignment;
        cout << "\tFinal exam: " << best->final << endl;
    }
};

int main()
{
    class_room();
}