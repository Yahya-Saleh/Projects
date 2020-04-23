#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        //checking whether the user inputed an integer
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            if (isdigit(argv[1][i]) == false)
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }
        //changing the argv[1] string into an integer variable
        int k = atoi(argv[1]);
        //getting plaintext
        string plain = get_string("plaintext: ");
        for (int i = 0, n = strlen(plain); i < n; i++)
        {
            //is the current letter an alphabet
            if (isalpha(plain[i]))
            {
                //keeping in mind the capitalization
                if (islower(plain[i]))
                {
                    plain[i] = 97 + (((plain[i] - 97) + k) % 26);
                }
                else
                {
                    plain[i] = 65 + (((plain[i] - 65) + k) % 26); 
                }
            }
        }
        printf("ciphertext: %s\n", plain);
        return 0;
    }
    //if the user doesn't give exactly one additional command
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}
