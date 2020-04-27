#include <cs50.c>
#include <stdio.h>

void hash(int n);

int main(void)
{
    //getting the accurate height
    int h;
    do
    {
        h = get_int("Height (1-8): ");
    }
    while (h < 1 || h > 8);
    
    //for every level of the pyramid of height h
    for (int i = 0; i < h; i++)
    {
        //printing the space to get the left pyramid form
        for (int y = h - 1 - i; y > 0; y--)
        {
            printf(" ");
        }
        //printing the hashes of the left pyramid
        hash(i);
        
        //a space saperating the right and left pyramid
        printf(" ");
        
        //printing the hashes of the right pyramid
        hash(i);

        //starting a new line for a new level
        //this will leave an extra line after the last level
        printf("\n");
    }
}
//print # n times
void hash(int n)
{
    for (int x = -1; x < n; x++)
    {
        printf("#");
    }
}