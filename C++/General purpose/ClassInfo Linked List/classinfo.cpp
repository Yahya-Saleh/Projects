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
    student *tail = NULL;
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
            cout << "Welcome to class CLI:\n\t\
            1. Add new records\n\t\
            2. Add a record\n\t\
            3. Display records\n\t\
            4. Get best student\n\t\
            5. Search record\n\t\
            6. Update record\n\t\
            7. Delete record\n\t\
            8. Rest\n\n\t\
            0. Exit\n";
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
            else if (option == 5)
            {
                cout << "Enter the student's ID: ";
                int id;
                cin >> id;
                student *stud = search_record(id);

                if (stud)
                    display_student(stud);
                else
                    cout << "No student with " << id << " ID.";
            }
            else if (option == 6)
            {
                cout << "Enter the student's ID: ";
                int id;
                cin >> id;
                student *stud = search_record(id);

                if (stud)
                    update_record(stud);
                else
                    cout << "No student with " << id << " ID.";
            }
            else if (option == 7)
            {
                cout << "Enter the student's ID: ";
                int id;
                cin >> id;
                bool deleted = delete_record(id);
                if (!deleted)
                    cout << "No student with " << id << " ID.";
                else
                    cout << "successfully deleted";
            }
            else if (option == 8)
                rest();
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
        {
            head = stud;
            tail = stud;
        }
        else
        {
            tail->next = stud;
            tail = stud;
        }
    }

    void display_student(student *stud)
    {
        cout << "\tID: " << stud->stud_id;
        cout << "\tMidterm-test: " << stud->test;
        cout << "\tQuiz: " << stud->quiz;
        cout << "\tAssignment: " << stud->assignment;
        cout << "\tFinal exam: " << stud->final << endl;
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
            display_student(trv);
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

    student *search_record(int id)
    {
        for (student *trv = head; trv != NULL; trv = trv->next)
            if (trv->stud_id == id)
                return trv;

        return NULL;
    }

    void update_record(student *stud)
    {
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
    }

    bool delete_record(int id)
    {
        student *prv = NULL;
        for (student *trv = head; trv != NULL; trv = trv->next)
        {
            if (trv->stud_id == id)
            {
                if (!prv)
                    head = trv->next;
                else
                    prv->next = trv->next;
                delete trv;
                return true;
            }
            prv = trv;
        }
        return false;
    }

    void rest()
    {
        student *next = NULL;
        student *trv = head;
        while (trv != NULL)
        {
            next = trv->next;
            delete trv;
            trv = next;
        }

        head = NULL;
    }
};

int main()
{
    class_room();
}