/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   radix_sort.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-01-12 17:32:45 by sabo-gla          #+#    #+#             */
/*   Updated: 2026-01-12 17:32:45 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	get_max_bits(t_stack *stack)
{
	t_node	*head;
	int		max;
	int		max_bits;

	head = stack->top;
	max = head->value;
	while (head)
	{
		if (head->value > max)
			max = head->value;
		head = head->next;
	}
	max_bits = 0;
	while ((max >> max_bits) != 0)
		max_bits++;
	return (max_bits);
}

int	is_sorted(t_stack *stack)
{
	t_node	*curr;

	curr = stack->top;
	while (curr && curr->next)
	{
		if (curr->value > curr->next->value)
			return (0);
		curr = curr->next;
	}
	return (1);
}

static void	radix_pass(t_stack *stack_a, t_stack *stack_b, int bit, int size)
{
	int		j;
	t_node	*head_a;

	j = 0;
	while (j < size)
	{
		head_a = stack_a->top;
		if (((head_a->value >> bit) & 1) == 1)
			ra(stack_a);
		else
			pb(stack_b, stack_a);
		j++;
	}
}

void	radix_sort(t_stack *stack_a, t_stack *stack_b)
{
	int	i;
	int	size;
	int	max_bits;

	size = stack_a->size;
	max_bits = get_max_bits(stack_a);
	i = 0;
	while (i < max_bits)
	{
		radix_pass(stack_a, stack_b, i, size);
		while (stack_b->size > 0)
			pa(stack_a, stack_b);
		if (is_sorted(stack_a) && stack_b->size == 0)
			return ;
		i++;
	}
}
