#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head node
 * @number: inserted number
 * Return: address of new node, NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr;
	listint_t *new_node;
	int start;

	ptr = *head;
	start = 0;
	new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);
	if (!ptr && !head)
		return (NULL);
	else if (!*head)
	{
		*head = new_node;
		new_node->n = number;
		new_node->next = NULL;
		return (new_node);
	}
	else if (number < ptr->n)
		start = 1;
	while (ptr->next && number > ptr->next->n && !start)
		ptr = ptr->next;
	if (!start)
	{
		new_node->next = ptr->next;
		ptr->next = new_node;
	}
	else
	{
		new_node->next = ptr;
		*head = new_node;
	}
	new_node->n = number;
	return (new_node);
}
