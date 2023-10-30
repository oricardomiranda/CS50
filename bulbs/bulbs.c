#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    string phrase = get_string("Message: ");

    for (int i = 0; i < strlen(phrase); i++)
    {
        int ascii_value = (int) phrase[i];

        for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
        {
            int bit = (ascii_value >> j) & 1;

            print_bulb(bit);

            // Print a space after every bit except the last one
            if (j != 0)
            {
                printf("");
            }
        }

        // Print a line break after every byte (8 bits)
        printf("\n");
    }

    return 0;
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
