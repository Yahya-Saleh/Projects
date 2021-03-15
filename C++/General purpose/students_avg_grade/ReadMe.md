# Students' grades

A program that prompts the user for the number of their students and creates an array of that size. Then using pointers and dynamic memory the program prompts the user to enter a grade for each student in each of the three categories:

- Quiz out of 20
- Assignment out of 30
- Final exam out of 50

If the user provides a value out of range the system will prompt them again after displaying an error message. Finally, the program will print out the average grade of the students.

## Execution

### 1

```bash
Enter the number of students: 1
Enter grades for student 1
   Quiz grade (out of 20): 21
   Enter a grade within range!
   Quiz grade (out of 20): -1
   Enter a grade within range!
   Quiz grade (out of 20): 12
   Assignment grade (out of 30): 29
   Final exam grade (out of 50): -1
   Enter a grade within range!
   Final exam grade (out of 50): 50
The average grade in this class is 91
```

### 5

```bash
Enter the number of students: 5
Enter grades for student 1
   Quiz grade (out of 20): 19
   Assignment grade (out of 30): 21
   Final exam grade (out of 50): 50
Enter grades for student 2
   Quiz grade (out of 20): 13
   Assignment grade (out of 30): 31
   Enter a grade within range!
   Assignment grade (out of 30): 21
   Final exam grade (out of 50): 50
Enter grades for student 3
   Quiz grade (out of 20): 20
   Assignment grade (out of 30): 30
   Final exam grade (out of 50): 50
Enter grades for student 4
   Quiz grade (out of 20): 20
   Assignment grade (out of 30): 30
   Final exam grade (out of 50): 50
Enter grades for student 5
   Quiz grade (out of 20): 17
   Assignment grade (out of 30): 28
   Final exam grade (out of 50): 40
The average grade in this class is 91.8
```
