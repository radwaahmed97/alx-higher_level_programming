#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *present, *status;

	if (list == NULL || list->next == NULL)
		return (0);
	present = list;
	status = present->next;

	while (present != NULL && status->next != NULL
		&& status->next->next != NULL)
	{
		if (present == status)
			return (1);
		status = present->next;
		status = status->next->next;
	}
	return (0);
}
