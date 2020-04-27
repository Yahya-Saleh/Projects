#include<stdio.h>
#include<cs50.c>
#include<math.h>

int main(void)
{
    //variable declared outside to mind the scope
    float f;
    //getting a positive integer
    do
    {
        f = get_float("change owed: ");
    }
    while (f < 0);
    
    //rounding to the nearest hunder after multiplying by a hunder to make change an int
    int change = round(f * 100);
    
    //how many quarters in change 
    int q = change / 25;
    int d = ((change - (q * 25)) / 10);
    int n = ((change - (q * 25) - (d * 10)) / 5);
    int p = ((change - (q * 25) - (d * 10) - (n * 5)) / 1);
    printf("number of coins: %i\n", q + d + n + p);
}
