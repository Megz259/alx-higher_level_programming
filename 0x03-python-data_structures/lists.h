#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked lists
 * @i: integer
 * @nn: next node
 *
 */

typedef struct listint_s
{
	int i;
	struct listint_s *nn;
} listint_t;

int is_palindrome(listint_t **head);
def print_list_integer(my_list=[]);

#endif
