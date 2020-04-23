#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    //checking for proper use
    if (argc != 4)
    {
        printf("Usage: ./resize f infile outfile\n");
        return 1;
    }

    //getting our float
    float f = atof(argv[1]);

    //checking for proper float
    if (f > 100 || f <= 0)
    {
        printf("the float must be within the range of (0.0,100.0]\n");
        return 2;
    }

    //opening the given files
    FILE *infile = fopen(argv[2], "r");
    //checking if the file exists
    if (!infile)
    {
        printf("couldn't open %s.\n", argv[2]);
        return 3;
    }

    //creating the out file
    FILE *outfile = fopen(argv[3], "w");
    //checking if the file can be created
    if (!outfile)
    {
        printf("couldn't create %s.\n", argv[3]);
        return 4;
    }

    //reading the bit map's file and info headers
    BITMAPFILEHEADER bf;
    BITMAPINFOHEADER bi;

    fread(&bf, sizeof(BITMAPFILEHEADER), 1, infile);
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, infile);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 || bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(infile);
        fclose(outfile);
        printf("not supported file format\n");
        return 5;
    }

    //calaculating the padding of the infile to skip over
    int inpadding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    //adjusting the headers to hold the new bit map
    bi.biWidth *= f;
    bi.biHeight *= f;

    //calculating the padding of the outfile
    int outpadding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    //using the outfile's padding we resume the adjustment
    bi.biSizeImage = ((sizeof(RGBTRIPLE) * bi.biWidth) + outpadding) * abs(bi.biHeight);
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    //copying the bit map's file and info headers to the outfile
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outfile);
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outfile);

    //returning the values back
    int biw = bi.biWidth / f;
    int bih = fabsf(bi.biHeight / f);

    // iterate over infile's scanlines
    if (f >= 1)
    {
        for (int i = 0; i < bih; i++)
        {
            RGBTRIPLE *prgb = malloc(sizeof(RGBTRIPLE) * biw);

            // iterate over pixels in scanline
            for (int j = 0; j < biw; j++)
            {
                // temporary storage
                RGBTRIPLE triple;

                // read RGB triple from infile
                fread(&triple, sizeof(RGBTRIPLE), 1, infile);

                prgb[j] = triple;

                //iterating RGB pixel f times
                for (int k = 0; k < f; k++)
                {
                    // write RGB triple to outfile
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outfile);
                }
            }

            // skip over padding, if any
            fseek(infile, inpadding, SEEK_CUR);

            // then add it back (to demonstrate how)
            for (int j = 0; j < outpadding; j++)
            {
                fputc(0x00, outfile);
            }

            for (int z = 0; z < f - 1; z++)
            {
                for (int j = 0; j < biw; j++)
                {
                    for (int k = 0; k < f; k++)
                    {
                        fwrite(&prgb[j], sizeof(RGBTRIPLE), 1, outfile);
                    }
                }

                for (int j = 0; j < outpadding; j++)
                {
                    fputc(0x00, outfile);
                }
            }

            free(prgb);
        }
    }

    else
    {
        int skip = pow(f, -1) - 1;

        for (int i = 0; i < bih; i++)
        {
            for (int j = 0; j < biw; j++)
            {
                RGBTRIPLE triple;

                fread(&triple, sizeof(RGBTRIPLE), 1, infile);

                fwrite(&triple, sizeof(RGBTRIPLE), 1, outfile);

                fseek(infile, skip * 3, SEEK_CUR);
                j += skip;
            }

            // skip over padding, if any
            fseek(infile, inpadding, SEEK_CUR);

            //add outfile's padding
            for (int j = 0; j < outpadding; j++)
            {
                fputc(0x00, outfile);
            }

            for (int j = 0; j < skip; j++)
            {
                fseek(infile, biw * 3, SEEK_CUR);

                // skip over padding, if any
                fseek(infile, inpadding, SEEK_CUR);
            }

            i += skip;
        }
    }

    fclose(infile);
    fclose(outfile);

    return 0;
}