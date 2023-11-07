// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

//https://cs50.harvard.edu/x/2023/problems/2/no-vowels/

#include <cs50.h>
#include <stdio.h>
#include <string.h>

char* replace(const char* input)
{
    static char output[100]; // Adjust the size as needed
    int length = strlen(input);

    for (int i = 0; i < length; i++)
    {
        switch (input[i])
        {
            case 'a':
            case 'A':
                output[i] = '4';
                break;
            case 'e':
            case 'E':
                output[i] = '3';
                break;
            case 'i':
            case 'I':
                output[i] = '1';
                break;
            case 'o':
            case 'O':
                output[i] = '0';
                break;
            default:
                output[i] = input[i];
                break;
        }
    }
    output[length] = '\0';
    return output;
}

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s <input:string>\n", argv[0]);
        return 1;
    }

    string input = argv[1]; // Use string type for input
    char* leetOutput = replace(input);

    printf("%s", leetOutput);

    return 0;
}
