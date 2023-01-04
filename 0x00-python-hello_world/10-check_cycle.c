#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks cycle of linked list
 * @list: input
 * Return: 0 if no cycle, 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	if (list == NULL)
		exit(0);
	while (1)
	{
		if (first == NULL)
			return (0);
		first = first->next;
		second = second->next->next;
		if (first->next == NULL || second->next->next == NULL)
			return (0);
		else if (first->next == second->next->next)
			return (1);
	}
}
