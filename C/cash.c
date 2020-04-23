#include<stdio.h>
#include<cs50.h>
#include<math.h>

int main(void)
{
    float f;
    do
    {
        f = get_float("change owed: ");
    }
    while (f < 0);
    
    int c = round(f * 100);
    
    int q = c / 25;
    int d = ((c - (q * 25)) / 10);
    int n = ((c - (q * 25) - (d * 10)) / 5);
    int p = ((c - (q * 25) - (d * 10) - (n * 5)) / 1);
    printf("%i\n", q + d + n + p);
}
