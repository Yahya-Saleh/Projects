#include <cs50.h>
#include <stdio.h>

void hash(int n);

int main(void)
{
    int h;
    do
    {
        h = get_int("Height (1-8): ");
    }
    while (h < 1 || h > 8);
    
    for (int i = 0; i < h; i++)
    {
        for (int y = h - 1 - i; y > 0; y--)
        {
            printf(" ");
        }
        hash(i);
        
        printf(" ");
            
        hash(i);
        printf("\n");
    }
}
void hash(int n)
{
    for (int x = -1; x < n; x++)
    {
        printf("#");
    }
}
