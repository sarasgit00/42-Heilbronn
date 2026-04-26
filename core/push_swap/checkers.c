/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checkers.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025-12-16 19:49:04 by sabo-gla          #+#    #+#             */
/*   Updated: 2025-12-16 19:49:04 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	is_number(const char *str)
{
	int	index;

	if (!str || str[0] == '\0')
		return (0);
	index = 0;
	if (str[index] == '+' || str[index] == '-')
		index++;
	if (str[index] == '\0')
		return (0);
	while (str[index] != '\0')
	{
		if (str[index] < '0' || str[index] > '9')
			return (0);
		index++;
	}
	return (1);
}

int	is_int_range(long value)
{
	if (value < INT_MIN || value > INT_MAX)
		return (0);
	return (1);
}

int	has_duplicate(t_stack *stack, int number_to_check)
{
	t_node	*wander_current;

	wander_current = stack->top;
	while (wander_current != NULL)
	{
		if (wander_current->value == number_to_check)
		{
			return (1);
		}
		wander_current = wander_current->next;
	}
	return (0);
}
//wander_current zeigt jz auf top node, Zeile 46

void	errormsg_exit(void)
{
	write(2, "Error\n", 6);
	exit(1);
}
