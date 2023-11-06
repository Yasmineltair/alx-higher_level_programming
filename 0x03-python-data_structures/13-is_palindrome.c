#include "lists.h"

/**
  * is_palindrome - function check if list
  * is plindrome
  * @head: header
  * Return: 0 if it's not and 1 if it's
  */

int is_palindrome(listint_t **head)
{
if (head == NULL || *head == NULL)
	return (0);
return (plindrome(head, *head));
}

/**
  * plindrome - function to know if plindrome
  * @head: header of a list
  * @end: the end of a list
  * Return: 1 if plindrome
  */

int plindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (plindrome(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
