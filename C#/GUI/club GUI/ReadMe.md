# Club Management GUI

A neatly designed GUI that allows students, club representatives, and Administrators to Query and handle a university's club database accordingly. [Watch it in action!](https://youtu.be/8Q_wApPYiU8)

## Usage

To run the GUI add **Guna2** to your VS, and sure that you adjust the connection in the sql class to match that of the associated database.

## Table of content

- [Club Management GUI](#club-management-gui)
  - [Usage](#usage)
  - [Table of content](#table-of-content)
  - [Login Form](#login-form)
  - [Student Form](#student-form)
  - [Student representative form](#student-representative-form)
  - [Admin form](#admin-form)

## Login Form

![log in](../../../Snippets/C%20sharp/GUI/club%20GUI/login.gif)

This is the first form that a user will interact with. Upon entering there information, the system will query that info and grants them access. The system is smart enough to recognize wether a student is representing a club or not.

## Student Form

![Student page](../../../Snippets/C%20sharp/GUI/club%20GUI/Student%20form.gif)

In this form a student has access to all of the information of any given club, and they can apply to that club.

## Student representative form

![student representative](../../../Snippets/C%20sharp/GUI/club%20GUI/Club-representitive%20form.gif)

This form is for club representatives where they can update the group's description or logo, post updates and achievements, and send notification to the club members.

Since they also are students they can search and read about other clubs.

## Admin form

![admin form](../../../Snippets/C%20sharp/GUI/club%20GUI/admin%20form.gif)

The admin has access to the entire system. They can query the database, generate club details report and an activities report, add and update clubs, and delete or suspend inactive clubs.
