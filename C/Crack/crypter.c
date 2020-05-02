#include <crypt.h>
#include <string.h>
#include <cs50.c>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc != 3)
    {
        printf("Usage: ./crypter salt word\n");
    }

    printf("%s\n", crypt(argv[2], argv[1]));
}