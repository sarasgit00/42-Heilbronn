/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_operations.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025-12-16 15:18:11 by sabo-gla          #+#    #+#             */
/*   Updated: 2025-12-16 15:18:11 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	push(t_stack *src_stack, t_stack *dest_stack)
{
	t_node	*tmp;

	if (!src_stack || !dest_stack || src_stack->top == NULL)
		return ;
	tmp = src_stack->top;
	src_stack->top = src_stack->top->next;
	tmp->next = dest_stack->top;
	dest_stack->top = tmp;
	src_stack->size--;
	dest_stack->size++;
}

void	swap(t_stack *stack)
{
	int	tmp;

	if (!stack || !stack->top || !stack->top->next)
		return ;
	tmp = stack->top->value;
	stack->top->value = stack->top->next->value;
	stack->top->next->value = tmp;
}

void	rotate(t_stack *stack)
{
	int		tmp;
	t_node	*node;

	if (!stack || !stack->top || !stack->top->next)
		return ;
	node = stack->top;
	tmp = stack->top->value;
	while (node->next != NULL)
	{
		node->value = node->next->value;
		node = node->next;
	}
	node->value = tmp;
}
// 	Du springst also von einem Node zum nächsten Node.

// ----- Was ist node->next?

// node->next ist ein Pointer, der im aktuellen Node gespeichert ist.
// Er zeigt auf den nächsten Knoten der Liste.

// ------ Was passiert also technisch?

// Rechts: node->next liefert die Adresse des nächsten Knotens.

// Links: node = ... speichert diese Adresse in node.

// Dadurch zeigt node(wnader-pointer) ab jetzt auf diesen nächsten Knoten.
//
//
// [7] -> [9] -> [2] -> [5] -> NULL
//  ^
//  node

//  [7] -> [9] -> [2] -> [5] -> NULL
//         ^
//         node

void	reverse_rotate(t_stack *stack)
{
	t_node	*prev;
	t_node	*last;

	if (!stack || !stack->top || !stack->top->next)
		return ;
	prev = NULL;
	last = stack->top;
	while (last->next != NULL)
	{
		prev = last;
		last = last->next;
	}
	prev->next = NULL;
	last->next = stack->top;
}

// #include "../include/push_swap.h"

// void    rotate(t_stack *stack)
// {
//     t_node  *first;
//     t_node  *last;

//     if (!stack || !stack->top || !stack->top->next)
//         return ;
//     first = stack->top;
//     last = stack->top;
//     while (last->next)
//         last = last->next;
//     stack->top = first->next;
//     first->next = NULL;
//     last->next = first;
// }

// void	reverse_rotate(t_stack *stack)
// {
// 	int	tmp;
// 	t_node *node;

// 	node = stack->top;
// 	while (node->next != NULL)
// 	{
// 		tmp = node->next->value;
// 		node->next->value = node->value;
// 		node->value = tmp;
// 	}
// }

// void	reverse_rotate(t_stack *stack)
// {
// 	t_node *node;
// 	int last_value;
// 	int tmp;

// 	if(!stack || !stack->top || !stack->top->next)
// 		return ;
// 	node = stack->top;
// 	while( node->next != NULL)
// 	{
// 		node = node->next;
// 	}
// 	last_value = node->value;
// 	node = stack->top;
// 	while (node->next != NULL)
// 	{
// 		tmp = node->value;
// 		node->value = last_value;
// 		last_value = tmp;
// 		node = node->next;
// 	}
// 	// letzter Node bekommt den zweitletzten Wert (already done)
// }
