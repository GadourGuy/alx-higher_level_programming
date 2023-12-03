#include "lists.h"

/**
 * reverse_listint - reverses a listint_t linked list.
 * @head: head to be reversed
 *
 * Return: pointer to the first node of the reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = NULL, *tmp = NULL;

	if (head == NULL || *head == NULL)
		return (NULL);
	current = *head;
	*head = NULL;
	while (current != NULL)
	{
		tmp = current->next;
		current->next = *head;
		*head = current;
		current = tmp;
	}
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: list to be checked
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *reverse = *head;

	if (head == NULL || *head == NULL)
		return (1);
	reverse = reverse_listint(head);
	while (*head != NULL)
	{
		if ((*head)->n != reverse->n)
			return (0);
		*head = (*head)->next;
		reverse = reverse->next;
	}
	return (1);
}
