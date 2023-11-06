#include <stdlib.h>
#include <stdio.h>
#include "lists.h"


/**
  * slistint_length - Counts the number of elements in a linked list
  * @head: The linked list to count
  *
  * Return: Number of elements in the linked list
  */
int listint_length(const listint_t *head)
{
        int length = 0;

        while (head != NULL)
        {
                ++length;
                head = head->next;
        }

        return (length);
}


/**
  * is_palindrome - Checks if a singly linked list is a palindrome
  * @head: The head of the singly linked list
  *
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */
int is_palindrome(listint_t **head)
{
	listint_t *start = NULL, *finish = NULL;
	unsigned int i = 0, length = 0, length_cycle = 0, length_list = 0;

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);

	start = *head;
	length = listint_length(start);
	length_cycle = length * 2;
	length_list = length_cycle - 2;
	finish = *head;

	for (; i < length_cycle; i = i + 2)
	{
		if (start[i].n != finish[length_list].n)
			return (0);

		length_list = length_list - 2;
	}

	return (1);
}

/**
  * get_nodeint_at_index - Gets a node from a linked list
  * @head: The head of the linked list
  * @index: The index to find in the linked list
  *
  * Return: The specific node of the linked list
  */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *present = head;
	unsigned int iteration_times = 0;

	if (head)
	{
		while (present != NULL)
		{
			if (iteration_times == index)
				return (present);

			present = present->next;
			++iteration_times;
		}
	}

	return (NULL);
}
