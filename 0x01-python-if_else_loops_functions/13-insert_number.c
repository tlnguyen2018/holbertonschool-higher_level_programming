#include "lists.h"
/**
 *insert_node - entry point
 *Description: insert new node into a sorted linked list
 *@number: inserted value
 *@head: head
 *Return: 0 or 1
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *prev = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	if (new != NULL)
	{
		new->n = number;
		new->next = *head;
		if (new->next == NULL || new->n <= (*head)->n)
			*head = new;
		while (new->next && new->n > new->next->n)
		{
			prev = new->next;
			new->next = prev->next;
		}
		if (prev != NULL)
			prev->next = new;
	}
	return (new);
}
