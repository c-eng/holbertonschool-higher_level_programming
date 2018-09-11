#include "lists.h"

/**
 * check_cycle - checks if there is a loop within a singly linked list
 *
 * @list: list to be checked for loops
 *
 * Return: 1 if a loop is encountered, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *strider;

	if (!list)
		return (0);
	strider = list;
	while (strider->next)
	{
		list = list->next;
		strider = strider->next;
		if (!(strider->next))
			return (0);
		else
			strider = strider->next;
		if (list == strider)
			return (1);
	}
	return (0);
}
