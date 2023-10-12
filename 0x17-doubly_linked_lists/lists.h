#ifndef _LISTS_H_
#define _LISTS_H_

/* include header files */
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * struct dlistint_s - function that defines a doubly linked list
 * @prev: pointer to previous node
 * @next: pointer to next node
 * @n: data
 */

typedef struct dlistint_s
{
	int n;
	struct dlistint_s *prev;
	struct dlistint_s *next;
} dlistint_t;


/* PROTOTYPES */
size_t print_dlistint(const dlistint_t *h);



#endif /* lists.h */
