#include "lists.h"
#include <stdlib.h>
/**
* new_node - function that creates a new node.
* @number: valued to be inserted in linked list
* Return: Address of new_node
*/
listint_t *new_node(int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	new_node->n = number;
	new_node->next = NULL;

	return (new_node);

}
/**
* get_greater_than_node - function that gets node with n value greater than
* number
* @node: node of linked list.
* @number: valued to be inserted in linked list
* Return: Address of new_node
*/
listint_t *get_greater_than_node(listint_t *node, int number)
{
	listint_t *add_node = new_node(number);

	if (node->next == NULL && node->n < number)
	{
		node->next = add_node;
		return (add_node);
	}
	if (node->next->n < number)
		get_greater_than_node(node->next, number);
	else
	{
		add_node->next = node->next;
		node->next = add_node;
	}
	return (add_node);
}
/**
* insert_node - function that inserts a number into a singly linked list.
* @head: first node of linked list.
* @number: valued to be inserted in linked list
* Return: Address of new_node
*/
listint_t *insert_node(listint_t **head, int number)
{
	if (*head == NULL)
	{
		*head = new_node(number);
		return (*head);
	}
	return (get_greater_than_node(*head, number));
}
