#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long creditCardNumber;
    creditCardNumber = get_int("Please add your credit card number: ");
    int sum = 0;
    int doubleDigit = 1; //To start from second to last
    while (creditCardNumber > 0)
    {
        //Last digit
        int digit = creditCardNumber % 10;
        //Multiply
        if (doubleDigit)
        {
            digit *= 2;
            while (digit > 0)
            {
                sum += digit % 10; //Sum the last digit
                digit /= 10; //Remove a digit
            }

        }//Mistery from here
        else
        {
            sum += digit;
        }

        // Toggle the flag for doubling
        doubleDigit = !doubleDigit;

        // Remove the last digit
        creditCardNumber /= 10;
    }

    printf("Sum of the digits: %d\n", sum);

    return 0;
}
    }
}