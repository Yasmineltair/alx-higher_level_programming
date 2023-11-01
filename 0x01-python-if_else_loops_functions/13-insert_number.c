#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
  * insert_node -  inserts a number into a sorted singly linked list
  * @head: first element
  * @number: inserted number
  * Return: the address of the new node
  */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node = malloc(sizeof(listint_t));
listint_t *temp = *head;

if (!new_node)
	return (NULL);
new_node->next = NULL;
new_node->n = number;
if (!temp || new_node->n < temp->n)
{
	new_node->next = temp;
	return (*head = new_node);
}
while (temp)
{
	if (!temp->next || new_node->n < temp->next->n)
	{
		new_node->next = temp->next;
		temp->next = new_node;
		return (temp);
	}
	temp = temp->next;
}
return (NULL);
}
