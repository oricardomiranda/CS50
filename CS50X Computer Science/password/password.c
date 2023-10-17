#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

bool has_uppercase(const char *password);
bool has_lowercase(const char *password);
bool has_digit(const char *password);
bool has_symbol(const char *password);

int main(void)
{
    string password = get_string("Enter your password: ");

    if (strlen(password) == 0)
    {
        printf("Please enter a password.\n");
        return 1;
    }

    bool valid_password = true;

    if (!has_uppercase(password))
    {
        printf("Your password needs at least one uppercase letter.\n");
        valid_password = false;
    }
    if (!has_lowercase(password))
    {
        printf("Your password needs at least one lowercase letter.\n");
        valid_password = false;
    }
    if (!has_digit(password))
    {
        printf("Your password needs at least one number.\n");
        valid_password = false;
    }
    if (!has_symbol(password))
    {
        printf("Your password needs at least one symbol.\n");
        valid_password = false;
    }

    if (valid_password)
    {
        printf("Your password is valid!\n");
    }
}

bool has_uppercase(const char *password)
{
    for (int i = 0; password[i] != '\0'; i++)
    {
        if (isupper(password[i]))
        {
            return true;
        }
    }
    return false;
}

bool has_lowercase(const char *password)
{
    for (int i = 0; password[i] != '\0'; i++)
    {
        if (islower(password[i]))
        {
            return true;
        }
    }
    return false;
}

bool has_digit(const char *password)
{
    for (int i = 0; password[i] != '\0'; i++)
    {
        if (isdigit(password[i]))
        {
            return true;
        }
    }
    return false;
}

bool has_symbol(const char *password)
{
    for (int i = 0; password[i] != '\0'; i++)
    {
        if (!isalnum(password[i]))
        {
            return true;
        }
    }
    return false;
}
