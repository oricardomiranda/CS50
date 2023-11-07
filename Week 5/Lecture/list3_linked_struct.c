#include <stdlib.h>
#include <stdio.h>

typedef struct node
{
	int number;
	struct node *next;
}
node;

int main(int argc, char *argv[])
{
	node *list = NULL; //Start of the list

	for (int i = 1; i < argc; i++)
	{
		int number = atoi(argv[i]);

		node *n = malloc(sizeof(node));
		if (n == NULL)
		{
			return 1;
		}

		n->number = number; //Attribute the argument number
		n->next = NULL; //Discard the pointer

		n->next = list; //Point to the next is list
		list = n;
	}

	node *ptr = list; //Temp pointer pointing to the first node in the list
	while (ptr != NULL)
	{
		printf("%i\n", ptr->number);
		ptr = ptr->next;
	}

	ptr = list;
	while (ptr != NULL)
	{
		node *next = ptr->next;
		free(ptr);
		ptr = next;
	}
}

//1h25m
