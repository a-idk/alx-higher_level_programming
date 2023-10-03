#include "lists.h"

/**
 * insert_node - function that inserts a number into
 * a sorted singly-linked list
 * @head: points to the start/head linked list.
 * @number: number to be inserted
 * @a_idk
 *
 * Return: pointer to new node, else NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	/* declaring and initializing variables */
	listint_t *nw; /* new node */
	listint_t *nd = *head;

	/* allocating dynamic memory */
	nw = malloc(sizeof(listint_t));
	/* checking for NULL value */
	if (nw == NULL)
		return (NULL);

	nw->n = number;

	if (nd == NULL || nd->n >= number)
	{
		nw->next = nd, *head = nw;
		return (nw);
	}

	while (nd && nd->next && nd->next->n < number)
	{
		nd = nd->next;
	}
	nw->next = nd->next, nd->next = nw;
	return (nw);
}
