#include <stdlib.h>
#include <stdio.h>

int main(void)
{
	int *list = malloc(3 * sizeof(int));
	if (list == NULL)
	{
		return 1;
	}

	list[0] = 1;
	list[1] = 2;
	list[2] = 3;

	//Second method to add memory
	int *tmp = realloc(list, 4* sizeof(int)); //This tmp is to temporarily deal with memory to deal with memory leaks
	if (tmp == NULL)
	{
		free(list);
		return 1;
	}
	list = tmp;

	list[3] = 4;

	for (int i = 0; i < 4; i++)
	{
		printf("%i\n", tmp[i]);
	}

	free(tmp);
	return 0;
}
