#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s image\n", argv[0]);
        return 1;
    }

    // Open forensic image
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        fprintf(stderr, "Could not open %s\n", argv[1]);
        return 1;
    }

    // Variables to keep track of JPEG file and count
    FILE *jpeg = NULL;
    char filename[8];
    int count = 0;

    // Read blocks of 512 bytes
    BYTE buffer[512];
    while (fread(buffer, sizeof(BYTE), 512, file) == 512)
    {
        // Check for JPEG signature
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close previous JPEG file if open
            if (jpeg != NULL)
            {
                fclose(jpeg);
            }

            // Create new JPEG file
            sprintf(filename, "%03i.jpg", count);
            jpeg = fopen(filename, "w");
            if (jpeg == NULL)
            {
                fclose(file);
                fprintf(stderr, "Could not create %s\n", filename);
                return 1;
            }

            count++;
        }

        // Write data to current JPEG file
        if (jpeg != NULL)
        {
            fwrite(buffer, sizeof(BYTE), 512, jpeg);
        }
    }

    // Close any remaining files
    if (jpeg != NULL)
    {
        fclose(jpeg);
    }

    // Close forensic image
    fclose(file);

    return 0;
}
