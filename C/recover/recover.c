#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    //checking for proper use
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");

        return 1;
    }

    //attempting to open the memory card
    FILE *memorycard = fopen(argv[1], "r");
    if (!memorycard)
    {
        fprintf(stderr, "Couldn't open %s\n", argv[1]);

        return 2;
    }

    //create a buffer to store what we read from the mc
    unsigned char *pbuffer = malloc(512);

    //Creating the counter for image name and the variable to hold the name
    int count = 0;
    char filename[8];

    int n = fread(pbuffer, 1, 512, memorycard);

    //reading until we reach EOF
    while (n == 512)
    {
        //checking if the block is the beginning of a JPEG file
        if (pbuffer[0] == 0xff && pbuffer[1] == 0xd8 && pbuffer[2] == 0xff && (pbuffer[3] & 0xf0) == 0xe0)
        {
            //creating the file's name and keeping count
            sprintf(filename, "%03i.jpg", count);
            count++;

            //opening a file to store the JPEG image
            FILE *img = fopen(filename, "w");
            if (!img)
            {
                fprintf(stderr, "couldn't create %s\n", filename);
                return 3;
            }

            //copying the image into the file until a new one is found
            do
            {
                fwrite(pbuffer, 1, 512, img);

                n = fread(pbuffer, 1, 512, memorycard);

                //while checking if the memory card is finished
                if (n != 512)
                {
                    free(pbuffer);
                    //success
                    return 0;
                }
            }
            while (pbuffer[0] != 0xff || pbuffer[1] != 0xd8 || pbuffer[2] != 0xff || (pbuffer[3] & 0xf0) != 0xe0);

            fclose(img);
        }

        else
        {
            n = fread(pbuffer, 1, 512, memorycard);
        }
    }
}

