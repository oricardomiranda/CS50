#include <cs50.h>
#include <stdio.h>

// Function to print spaces
void print_spaces(int count)
{
    for (int i = 0; i < count; i++)
    {
        printf(" ");
    }
}

// Function to print hashes
void print_hashes(int count)
{
    for (int i = 0; i < count; i++)
    {
        printf("#");
    }
}

int main(void)
{
    int height = 0;
    do
    {
        height = get_int("Choose a height between 1 and 8: ");
    }
    while (height < 1 || height > 8);

    for (int i = 1; i <= height; i++)
    {
        // Print spaces for left pyramid
        print_spaces(height - i);

        // Print hashes for left pyramid
        print_hashes(i);

        // Print gap between pyramids
        printf("  ");

        // Print hashes for right pyramid
        print_hashes(i);

        printf("\n");
    }
}
