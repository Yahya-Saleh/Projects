#include <stdio.h>
#include <cs50.c>
#include <string.h>
#include <ctype.h>

int shift(char c);

int main(int argc, string argv[])
{
    //if the user does not give exactly one additional command
    if (argc != 2)
    {
        printf("Usage: ./vigenere keyword\n");
        return 1;
    }

    int n = strlen(argv[1]);
    //creating an array to store all of the keywords after they become integers
    int key[n];
    //checking whether the user inputted a keyword
    for (int i = 0; i < n; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Usage: ./vigenere keyword\n");
            return 1;
        }
        //transforming the keywords into integers
        key[i] = shift(argv[1][i]);
    }

    //getting plaintext
    string plain = get_string(NULL, "plaintext: ");
    for (int i = 0, no = strlen(plain), j = 0; i < no; i++)
    {
        //we transform the character if and only if it's an alphabet
        if (isalpha(plain[i]))
        {
            //keeping in mind the capitalization
            if (islower(plain[i]))
            {
                plain[i] = 97 + (((plain[i] - 97) + key[j % n]) % 26);
            }
            else
            {
                plain[i] = 65 + (((plain[i] - 65) + key[j % n]) % 26); 
            }
            j += 1;
        }
    }

    printf("ciphertext: %s\n", plain);
    return 0;
}

int shift(char c)
{
    int k = 0;
    //ASCII code
    if (islower(c))
    {
        k = c - 97;
    }
    else
    {
        k = c - 65;
    }
    return k;
}
