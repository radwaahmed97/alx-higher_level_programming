#include "lists.h"
#include <stddef.h>


/**
 * reverse_listint - reverses linked list
 * @head: head node
 * Return: pointer to first node in reversed list
 */

void reverse_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *present = *head;
	listint_t *next = NULL;

	while (present)
	{
		next = present->next;
		present->next = previous;
		previous = present;
		present = next;
	}
	*head = previous;
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head node pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slo = *head, *fast = *head, *ptr = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slo->next;
			break;
		}
		slo = slo->next;
	}
	reverse_listint(&dup);

	while (dup && ptr)
	{
		if (ptr->n == dup->n)
		{
			dup = dup->next;
			ptr = ptr->next;
		}
		else
			return (0);
	}
	if (!dup)
		return (1);
	return (0);
}
