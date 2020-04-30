#include <crypt.h>
#include <string.h>
#include <cs50.h>
#include <stdio.h>


int main(int argc, string argv[])
{
    if (argc == 2)
    {
        //a library with all the alphabet
        char alpha[53] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
        //getting the salt
        char salt[3];
        for (int i = 0; i < 2; i++)
        {
            salt[i] = argv[1][i];
        }
        //our first guess that we will keep modifying
        char guess[5] = {'a', 'a', 'a', 'a', 'a'};
        //variables to modify the guess
        int a = 0, b = 0, c = 0, d = 0, e = 0;
        while (true)
        {   
            string hash = crypt(guess, salt);
            //check if both match
            bool tf = true;
            for (int i = 0, n = strlen(argv[1]); i < n; i++)
            {
                if (hash[i] != argv[1][i])
                {
                    tf = false;
                }
            }
            if (tf == true)
            {
                printf("%s\n", guess);
                return 0;
            }
            //shifting the last digit
            if (a == 52)
            {
                a = 0;
                b++;
                //after we are done with the last digit we modify the one before last
                if (b == 52)
                {
                    b = 0;
                    c++;
                    //the 3rd digit
                    if (c == 52)
                    {
                        c = 0;
                        d++;
                        //fourth digit
                        if (d == 52)
                        {
                            //the fifth digit
                            e++;
                            guess[0] = alpha[e];
                        }
                        guess[1] = alpha[d];
                    }
                    guess[2] = alpha[c];
                }
                guess[3] = alpha[b];
            }
            guess[4] = alpha[a];
            a++;
        }
    }
    //promting the user for accurate input
    else
    {
        printf("Usage: ./crack hash\n");
        return 1;
    }
}
