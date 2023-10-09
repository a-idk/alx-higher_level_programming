#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Function that reverses a
 * singly-linked listint_t list
 * @head: starting node pointer
 * @a_id coding
 *
 * Return: head pointer
 */

listint_t *reverse_listint(listint_t **head)
{
	/* initializing variables */
	listint_t *next;
	listint_t *node = *head;
	listint_t *prev = NULL;

	while (node)
		next = node->next, node->next = prev, prev = node, node = next;
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 * @a_idk coding
 *
 * Return: 0 if sucessful , else -1
 */

int is_palindrome(listint_t **head)
{
	/* declaring and initializing variables */
	size_t idx;
	size_t size;
	listint_t *mid;
	listint_t *rev;
	listint_t *temp;

	/* checking for NULL value */
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
		size += 1, temp = temp->next;
	temp = *head;
	for (idx = 0; idx < (size / 2) - 1; idx += 1)
		temp = temp->next;
	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);
	temp = temp->next->next, rev = reverse_listint(&temp), mid = rev;

	temp = *head;
	while (rev)
	{
		if (temp->n != rev->n)
			return (0);
		temp = temp->next, rev = rev->next;
	}
	reverse_listint(&mid);
	return (1);
}
