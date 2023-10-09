/* Title: is_palindrome.c */
/* include header file */

#include "lists.h"

/**
 * reverse_list_int - Function that reverses a
 * singly-linked listint_t list
 * @start: head pointer
 * @a_idk coding
 *
 * Return: head pointer
 */

listint_t *reverse_list_int(listint_t **start)
{
	/* defining variables */
	listint_t *node = *start;
	listint_t *next;
	listint_t *prev = NULL;

	while (node != NULL)
		next = node->next, node->next = prev, prev = node, node = next;
	*start = prev;
	return (*start);
}


/**
 * is_palindrome - a function in C that checks if a singly
 * linked list is a palindrome
 * @start: head pointer
 * @a_idk coding
 *
 * Return: 0 if successful, else -1
 */

int is_palindrome(listint_t **start)
{
	/* assigning variables */
	listint_t *rev;
	listint_t *temp;
	listint_t *midd;
	size_t size = 0;
	size_t idx;

	/* checking for NULL value */
	if ((*start == NULL) || ((*start)->next == NULL))
		return (1);

	/* for temp */
	temp = *start;
	while (temp != NULL)
		size += 1, temp = temp->next;

	temp = *start;
	for (idx = 0; (idx < (size / 2)); idx += 1)
		temp = temp->next;
	if ((temp->n != temp->next->n) && ((size % 2) == 0))
		return (0);
	temp = temp->next->next, rev = reverse_list_int(&temp), midd = rev;

	/* for rev */
	temp = *start;
	while (rev != NULL)
	{
		if (temp->n != rev->n)
			return (0);
		temp = temp->next, rev = rev->next;
	}
	reverse_list_int(&midd);
	return (1);
}
