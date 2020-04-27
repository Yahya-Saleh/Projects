#include <stdio.h>
#include <cs50.c>

int main(void)
{
    string name = get_string(NULL, "Enter your name\n");
    printf("Hello, %s\n", name);
}
