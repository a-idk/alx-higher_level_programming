/* title: 0-print_dlistint.c */

#include "lists.h"
#include <stdio.h>

/**
 * print_dlistint - function that prints all the elements of a
 * dlistint_t list
 * @h: node ptr
 * @a_idk coding
 *
 * Return: number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	/* initializing variable */
	size_t numbers_node = 0;

	while (h)
		printf("%d\n", h->n), h = h->next, numbers_node += 1;
	return (numbers_node);
}
