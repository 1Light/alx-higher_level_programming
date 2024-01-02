#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - outputs all elements of a listint_t list
 * @h: pointer to head of the list(first element)
 * Return: quantity of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n;
	/* quantity of nodes */
	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}
	return (n);
}

/**
 * add_nodeint - puts a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the beginning of the list
 * @n: integer placed in node
 * Return: if success - address of the new element
 *         else - NULL
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}

/**
 * free_listint - unleashes listint_t list
 * @head: pointer to the list released
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
