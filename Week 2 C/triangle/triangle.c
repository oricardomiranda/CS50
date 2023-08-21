/**
 * triangle.c
 * Doug Lloyd
 * lloyd@cs50.harvard.edu
 *
 * Validates a triangle
 *
 * Demonstrates use of CS50's library and functions
 * 
 * Take 3 lengths of a triangle's sides
 * 
 * A triangle may only have side with positive values
 * 
 * The sum of any two sides of the triangle must be greater than the length of the third side
 */


#include <cs50.h>
#include <stdio.h>
#include <stdbool.h>

// Declare function prototype
bool isValidTriangle(int a, int b, int c);

// isValidTriangle function
bool isValidTriangle(int a, int b, int c)
{
    // Check for negative side lengths
    if (a <= 0 || b <= 0 || c <= 0)
    {
        return false; // Invalid triangle
    }
    
    // Check the triangle inequality theorem using <= checks
    if ((a + b <= c) || (a + c <= b) || (b + c <= a))
    {
        return false; // Invalid triangle
    }
    
    return true; // Valid triangle
}

int main(void)
{
    // Ask user for input
    printf("Let's take the sides of your triangle: ");
    int a = get_int("Give me the first side: ");
    int b = get_int("Give me the second side: ");
    int c = get_int("Give me the third side: ");

    // Check the validity of the triangle using isValidTriangle function
    if (isValidTriangle(a, b, c))
    {
        printf("The triangle is valid!\n");
    }
    else
    {
        printf("The triangle is invalid!\n");
    }

    return 0;
}

