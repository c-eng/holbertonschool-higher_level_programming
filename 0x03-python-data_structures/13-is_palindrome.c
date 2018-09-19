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
 * _memcpy - copies n bytes from src to dest
 * @dest: bytes copied to
 * @src: bytes copied from
 * @n: number of bytes copied
 *
 * Return: pointer to dest
 */

char *_memcpy(char *dest, char *src, unsigned int n)
{
	unsigned int i;

	for (i = 0 ; i < n ; i++)
	{
		*(dest + i) = *(src + i);
	}

	return (dest);
}

/**
 * _realloc - realloc
 *
 * @ptr: memory to be reallocated
 * @size: size of memory of be reallocated
 *
 * Return: pointer to memory or NULL
 */

void *_realloc(void *ptr, size_t size)
{
	char *new_ptr = NULL;

	if (!ptr)
		return (malloc(size));
	if (!size)
	{
		free(ptr);
		return (NULL);
	}
	new_ptr = malloc(size);
	if (!new_ptr)
		return (NULL);
	_memcpy(new_ptr, ptr, size);
	free(ptr);
	return (new_ptr);
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
		array = _realloc(array, sizeof(int) * (idx + 1));
		if (!array)
			return (1);
		array[idx] = get_listint_at_index(*head, idx)->n;
		idx += 1;
		strider = strider->next;
	}
	for ( ; adx <= (idx / 2) ; adx++)
	{
		printf("%d, %d\n", array[adx], array[idx - adx - 1]);
		if (!(array[adx] == array[idx - adx - 1]))
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}