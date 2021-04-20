#include <iostream>
#include <string>

using namespace std;
bool isBalanced(string s);

class Stack
{
public:
    int top;
    unsigned capacity;
    char *array;

    Stack(unsigned capacity)
    {
        this->capacity = capacity;
        this->top = -1;
        this->array = new char[(this->capacity * sizeof(char))];
    }

    // Stack is full when top is equal to the last index
    int isFull() { return this->top == this->capacity - 1; }
    // Stack is empty when top is equal to -1
    int isEmpty() { return this->top == -1; }

    // Function to add an item to stack.
    // It increases top by 1
    void push(char item)
    {
        if (isFull())
            return;
        this->array[++this->top] = item;
    }

    // Function to remove an item from stack.
    // It decreases top by 1
    char pop()
    {
        if (isEmpty())
            return -1;
        return this->array[this->top--];
    }
};

int main()
{
    // Get the string
    string s;
    cout << "Enter a string with brackets: ";
    cin >> s;

    // Evaluate the bracket balance
    if (isBalanced(s))
        cout << "Brackets are balanced" << endl;
    else
        cout << "Brackets are not balanced" << endl;
}

bool isBalanced(string s)
{
    // Get the string size
    int size = s.size();
    // Create a stack of that size
    Stack *stack = new Stack(size);

    for (int i = 0; i < size; i++)
    {
        // If the ith character is an open bracket
        if (s[i] == '(' || s[i] == '{' || s[i] == '[')
            // Push it
            stack->push(s[i]);

        // Else if it is a closing bracket
        // compare its type to the last bracket added
        else if (s[i] == ')')
        {
            if (stack->pop() != '(')
                return false;
        }
        else if (s[i] == '}')
        {
            if (stack->pop() != '{')
                return false;
        }
        else if (s[i] == ']')
        {
            if (stack->pop() != '[')
                return false;
        }
    }

    // If all brackets have been addressed
    if (stack->isEmpty())
        return true;
    else
        return false;
}