#include <stdio.h>
#include <cs50.c>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    //if the user doesn't give exactly one additional command
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    //checking whether the user inputted an integer
    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        //for every char in the inputted string
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    //changing the inputted key string into an integer variable
    int key = atoi(argv[1]);

    //getting plaintext
    string plain = get_string(NULL, "plaintext: ");
    //changing plain text into ciphertext
    for (int i = 0, n = strlen(plain); i < n; i++)
    {
        //is the current letter an alphabet
        if (isalpha(plain[i]))
        {
            //keeping in mind the capitalization
            if (islower(plain[i]))
            {
                plain[i] = 97 + (((plain[i] - 97) + key) % 26);
            }
            else
            {
                plain[i] = 65 + (((plain[i] - 65) + key) % 26); 
            }
        }
    }
    
    printf("ciphertext: %s\n", plain);
    return 0;
}
