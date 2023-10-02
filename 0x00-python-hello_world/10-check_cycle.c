#include "lists.h"

/**
 * check_cycle - function that checks if a linked list
 * contains a cycle
 * @list: linked list to check
 * @a_idk
 *
 * Return: 1 if success, 0 otherwise
 */

int check_cycle(listint_t *lst)
{
	/* declaring variables */
	listint_t *tortoise = lst;
	listint_t *hare = lst;

	/* checking for NULL value */
	if (!lst)
		return (0);
	/* implementing Floyd's algorithm */
	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next, hare = hare->next->next;
		if (hare == tortoise)
			return (1);
	}
	return (0);
}
