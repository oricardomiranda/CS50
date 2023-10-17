#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int startSize;
    do
    {
        startSize = get_int("How many starting Llamas? ");
    }
    while (startSize < 9);

    // TODO: Prompt for end size
    int endSize;
    do
    {
        endSize = get_int("How many Llamas in the end? ");
    }
    while (endSize < startSize);

    // TODO: Calculate number of years until we reach threshold
    float currentSize = startSize;
    int years = 0;
    while (currentSize < endSize)
    {
        int growth = currentSize / 3;
        int attrition = currentSize / 4;
        // We add (growth - attrition) to the current size
        currentSize += (growth - attrition);
        years++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", years);

    return 0;
}
