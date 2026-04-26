/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   index_utils.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-01-07 21:29:24 by sabo-gla          #+#    #+#             */
/*   Updated: 2026-01-07 21:29:24 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	get_stack_size(t_stack *stack)
{
	int		size;
	t_node	*curr;

	size = 0;
	curr = stack->top;
	while (curr)
	{
		size++;
		curr = curr->next;
	}
	return (size);
}

static void	sort_array(int *arr, int size)
{
	int	i;
	int	j;
	int	temp;

	i = 0;
	while (i < size)
	{
		j = i + 1;
		while (j < size)
		{
			if (arr[i] > arr[j])
			{
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
			j++;
		}
		i++;
	}
}

static void	replace_with_index(t_node *curr, int *arr, int size)
{
	int	i;

	while (curr)
	{
		i = 0;
		while (i < size)
		{
			if (arr[i] == curr->value)
			{
				curr->value = i;
				break ;
			}
			i++;
		}
		curr = curr->next;
	}
}

static void	fill_array(int *arr, t_stack *stack)
{
	t_node	*curr;
	int		i;

	curr = stack->top;
	i = 0;
	while (curr)
	{
		arr[i++] = curr->value;
		curr = curr->next;
	}
}

void	assign_indices(t_stack *stack)
{
	int	*arr;
	int	size;

	size = get_stack_size(stack);
	arr = malloc(sizeof(int) * size);
	if (!arr)
		errormsg_exit();
	fill_array(arr, stack);
	sort_array(arr, size);
	replace_with_index(stack->top, arr, size);
	free(arr);
}
