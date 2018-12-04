#include "lists.h"
#include <stdio.h>
/**
 *check_cycle - entry point
 *Description: check if the linked list has cycle in it
 *@list: list of value
 *Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *afterhead;
	listint_t *head;

	head = list;
	afterhead = list;

	while (afterhead != NULL && afterhead->next != NULL)
	{
		head = head->next;
		afterhead = afterhead->next->next;
		if (head == afterhead)
			return (1);
	}
	return (0);
}
