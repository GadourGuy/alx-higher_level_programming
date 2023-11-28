#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted list
 * @head: head of list
 * @number: number to be inserted
 *
 * return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *new = malloc(sizeof(listint_t));

	if (*head)
	{
		while(tmp && tmp->next != NULL)
		{
			if (number > tmp->n && number < (tmp->next)->n)
			{
				new->next = tmp->next;
				tmp->next = new;
				new->n = number;
				return (new);
			}
			tmp = tmp->next;
		}
		return (NULL);
	}
	return (NULL);
}
