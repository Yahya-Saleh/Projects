#include <crypt.h>
#include <string.h>
#include <cs50.c>
#include <stdio.h>


int main(int argc, string argv[])
{
    // Promting the user for accurate input
    if (argc != 2)
    {
        printf("Usage: ./crack hash\n");
        return 1;
    }

    // Library with all the alphabet
    char alpha[53] = {'\0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

    // Getting the salt, i.e. first 2 characters
    char salt[3];
    memcpy(salt, argv[1], 2);
    salt[2] = '\0';

    // Our first guess that we will keep modifying
    char guess[6] = "\0\0\0\0\0\0";
    for (int a = 0; a < 53; a++)
    {
        for (int b = 0; b < 53; b++)
        {
            for (int c = 0; c < 53; c++)
            {
                for (int d = 0; d < 53; d++)
                {
                    for (int e = 1; e < 53; e++)
                    {
                        guess[0] = alpha[e];
                        guess[1] = alpha[d];
                        guess[2] = alpha[c];
                        guess[3] = alpha[b];
                        guess[4] = alpha[a];

                        if (strcmp(crypt(guess, salt), argv[1]) == 0)
                        {
                            printf("%s\n", guess);
                            return 0;
                        }
                    }
                }
            }
        }
    }

    // After trying all possible combinations
    printf("Password couldn't be cracked!");
    return 2;
}
