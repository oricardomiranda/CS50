#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

/*Implement your program in a file called readability.c in a directory called readability.
Your program must prompt the user for a string of text using get_string.

Your program should count the number of letters, words, and sentences in the text. You may assume that a letter is any lowercase
character from a to z or any uppercase character from A to Z, any sequence of characters separated by spaces should count as a word,
and that any occurrence of a period, exclamation point, or question mark indicates the end of a sentence.

Your program should print as output "Grade X" where X is the grade level computed by the Coleman-Liau formula, rounded to the
nearest integer.

If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level), your program
should output "Grade 16+" instead of giving the exact index number. If the index number is less than 1, your program should output
"Before Grade 1".
*/
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    int letters = 0;
    int words = 0;
    int sentences = 0;

    string text = get_string("Text: ");

    letters = count_letters(text);
    words = count_words(text);
    sentences = count_sentences(text);

    float L = ((float) letters / (float) words) * 100;
    float S = ((float) sentences / (float) words) * 100;

    int index = (int) (0.0588 * L - 0.296 * S - 15.8);

    if (index < 1)
        printf("Before Grade 1\n");
    else if (index > 16)
        printf("Grade 16+\n");
    else
        printf("Grade %i\n", index);
}

int count_letters(string text)
{
    // USE a for loop with strlen to sum all the letters using ascii table
    // return a letters variable to use in main
    int letters = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if ((i >= 'a' && i <= 'z') || (i <= 'A' && i <= 'Z'))
            letters++;
    }
    return letters;
}

int count_words(string text)
{
    // count words between spaces
    // we can assume no spaces in the beggining or end and no multiple spaces
    int words = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        while (i < strlen(text) && (text[i] == ' ' || text[i] == '\t'))
            i++;
        if (i < strlen(text))
            words++;
        while (i < strlen(text) && (text[i] == ' ' || text[i] == '\t'))
            i++;
    }
    return words;
}

int count_sentences(string text)
{
    // consider any sequence of characters that ends with . ? or !
    int sentences = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
            if (i == 0 || text[i - 1] == ' ' || text[i - 1] == '\t' || text[i - 1] == '\n')
                sentences++;
    }
    return sentences;
}