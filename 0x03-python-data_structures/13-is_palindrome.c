#include "lists.h"

/**
 * get_listint_at_index - returns nth node of a list
 *
 * @head: head of list
 * @index: index of node to return
 *
 * Return: node at nth index or NULL if it does not exist
 */

listint_t *get_listint_at_index(listint_t *head, unsigned int index)
{
	unsigned int idx = 0;

	while (head && idx < index)
	{
		idx++;
		head = head->next;
	}
	if (idx == index && head)
		return (head);
	return (NULL);
}

/**
 * is_palindrome - Checks if linked list is a palindrome
 *
 * @head: head of list to check
 *
 * Return: 1 if palindrome, else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *strider = NULL;
	size_t idx = 0, adx = 0;
	int *array = NULL;

	if (!head)
		return (0);
	if (!*head)
		return (1);
	strider = *head;
	while (strider)
	{
		array = realloc(array, sizeof(int) * (idx + 1));
		if (!array)
			return (1);
		array[idx] = get_listint_at_index(*head, idx)->n;
		idx += 1;
		strider = strider->next;
	}
	for ( ; adx <= (idx / 2) ; adx++)
	{
		if (!(array[adx] == array[idx - adx - 1]))
			free(array);
			return (0);
	}
	free(array);
	return (1);
}
