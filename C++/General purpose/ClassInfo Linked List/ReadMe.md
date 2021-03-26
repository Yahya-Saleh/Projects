# Class info Linked List

Defining a `class_room` class to hold and manage student nodes using a Linked List data structure.

## `Student` node

```c++
struct student
{
    int stud_id;
    int test, assignment,
        quiz, final;
    student *next = NULL;
};
```

## `class_room` class

The constructor of this class calls its menu method to start the CLI.

### `Menu`

This method is the essence of the class it executes the following menu indefinitely.

```bash
Welcome to class CLI:      
        1. Add new records 
        2. Add a record    
        3. Display records 
        4. Get best student

        0. Exit

Pick an option:
```

after the user gets teh output of the desired choice, the user is asked to press any key to continue which makes the display speed friend and trackable.

```bash
Press any key to continue...
```

### `new_record`

This method efficiently prompts teh user for the grades of a new student to add. Then it assigns an ID to the student and appends it to the LinkedList using the `append_student` method.

```bash
Enter the Midterm-test grade (out of 20): 21
Please enter a grade within range!
Enter the Midterm-test grade (out of 20): 23
Please enter a grade within range!
Enter the Midterm-test grade (out of 20): 20
Enter the Quiz grade (out of 10): 0
Enter the Assignment grade (out of 20): -1
Please enter a grade within range!
Enter the Assignment grade (out of 20): 20
Enter the Final exam grade (out of 50): 50

Press any key to continue...
```

### `new_records`

Runs the `new_record` method n times.

```bash
How many records fo you wish to: 3
Enter the information for student 1       

Enter the Midterm-test grade (out of 20): 20
Enter the Quiz grade (out of 10): 10
Enter the Assignment grade (out of 20): 20
Enter the Final exam grade (out of 50): 50


Enter the information for student 2       

Enter the Midterm-test grade (out of 20): 10
Enter the Quiz grade (out of 10): 2
Enter the Assignment grade (out of 20): 3
Enter the Final exam grade (out of 50): 4


Enter the information for student 3       

Enter the Midterm-test grade (out of 20): 0
Enter the Quiz grade (out of 10): 3
Enter the Assignment grade (out of 20): 9
Enter the Final exam grade (out of 50): 5
```

### `display_records`

As the name implies it displays the records of teh students

```bash
        ID: 0   Midterm-test: 20        Quiz: 10        Assignment: 20  Final exam: 50
        ID: 1   Midterm-test: 10        Quiz: 2 Assignment: 3   Final exam: 4
        ID: 2   Midterm-test: 0 Quiz: 3 Assignment: 9   Final exam: 5
```

### `best_student`

This method iterates over teh LinkedList and displays the student info that holds the best total score.

```bash
        ID: 0   Midterm-test: 20        Quiz: 10        Assignment: 20  Final exam: 50
```

---

## Execution

```bash
Welcome to class CLI:
        1. Add new records
        2. Add a record
        3. Display records
        4. Get best student

        0. Exit

Pick an option: 2
Enter the Midterm-test grade (out of 20): 2
Enter the Quiz grade (out of 10): 2
Enter the Assignment grade (out of 20): 2
Enter the Final exam grade (out of 50): 2

Press any key to continue...
Welcome to class CLI:      
        1. Add new records 
        2. Add a record    
        3. Display records 
        4. Get best student

        0. Exit

Pick an option: 3
        ID: 0   Midterm-test: 2 Quiz: 2 Assignment: 2   Final exam: 2

Press any key to continue...
Welcome to class CLI:     
        1. Add new records
        2. Add a record   
        3. Display records
        4. Get best student

        0. Exit

Pick an option: 2
Enter the Midterm-test grade (out of 20): 2
Enter the Quiz grade (out of 10): 2
Enter the Assignment grade (out of 20): 2
Enter the Final exam grade (out of 50): 2

Press any key to continue...
Welcome to class CLI:
        1. Add new records
        2. Add a record
        3. Display records
        4. Get best student

        0. Exit

Pick an option: 3
        ID: 0   Midterm-test: 2 Quiz: 2 Assignment: 2   Final exam: 2
        ID: 1   Midterm-test: 2 Quiz: 2 Assignment: 2   Final exam: 2

Press any key to continue...
Welcome to class CLI:
        1. Add new records
        2. Add a record
        3. Display records
        4. Get best student

        0. Exit

Pick an option: 4
        ID: 0   Midterm-test: 2 Quiz: 2 Assignment: 2   Final exam: 2

Press any key to continue...
Welcome to class CLI:
        1. Add new records
        2. Add a record
        3. Display records
        4. Get best student

        0. Exit

Pick an option: 2
Enter the Midterm-test grade (out of 20): 20
Enter the Quiz grade (out of 10): 10
Enter the Assignment grade (out of 20): 20
Enter the Final exam grade (out of 50): 30

Press any key to continue...
Welcome to class CLI:
        1. Add new records
        2. Add a record
        3. Display records
        4. Get best student

        0. Exit

Pick an option: 4
        ID: 2   Midterm-test: 20        Quiz: 10        Assignment: 20  Final exam: 30

Press any key to continue...
Welcome to class CLI:
        1. Add new records
        2. Add a record
        3. Display records
        4. Get best student

        0. Exit

Pick an option: 0
```
