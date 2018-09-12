#include "lists.h"

/**
 * insert_node - inserts a node into an ordered list
 *
 * @head: list head
 * @number: value of the new node
 *
 * Return: either the address of the new node or NULL on error
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *strider = *head;
	listint_t *add;

	if (!head)
		return (NULL);
	add = malloc(sizeof(listint_t));
	add->n = number;
	if (!*head)
	{
		add->next = NULL;
		*head = add;
		return (add);
	}
	if (strider->n > number)
	{
		add->next = *head;
		*head = add;
		return (add);
	}
	while (1)
	{
		if (strider->next)
		{
			if ((strider->next)->n > number)
			{
				add->next = strider->next;
				strider->next = add;
				return (add);
			}
			else
				strider = strider->next;
		}
		else
		{
			add->next = NULL;
			strider->next = add;
			return (add);
		}
	}
}
