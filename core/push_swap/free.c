/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   free.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-01-12 16:22:36 by sabo-gla          #+#    #+#             */
/*   Updated: 2026-01-12 16:22:36 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	free_stack_nodes(t_stack *stack)
{
	t_node	*tmp;

	while (stack->top)
	{
		tmp = stack->top->next;
		free(stack->top);
		stack->top = tmp;
	}
	stack->size = 0;
}
