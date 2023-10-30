#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * check_cycle - checks if a singly linked
  * list has a cycle in it.
  * @list: linked list
  * Return: 0 if there is no cycleand 1 if there is
  *
  */

int check_cycle(listint_t *list)
{
listint_t *first = list;
listint_t *second = list;

while (first && first->next)
{
	second = second->next;
	first = first->next->next;
	if (first == second)
		return (1);
}
return (0);
}
