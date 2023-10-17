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


// includes
#include <cs50.h>
#include <stdio.h>

// declare function prototype
int triangleValidator(int a, int b, int c);

// triangle function
int triangleValidator(int a, int b, int c)
{
	if ((a + b > c) && (a + c > b) && (b + c > a))
		return 1;
	else 
		return 0;
}

int main(void)
{
    // ask user for input
	printf("Let's take the sides of your triangle: ");
    int a = get_int("Give me the first side: ");
    int b = get_int("Give me the second side: ");
	int c = get_int("Give me the third side: ");

    // add the two numbers together via a function call
    
	if (triangleValidator(a, b, c))
    {
        printf("The triangle is valid!\n");
    }
    else
    {
        printf("The triangle is invalid!\n");
    }

    return 0;
}
