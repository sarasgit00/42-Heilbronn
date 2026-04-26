/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   initialize_stack.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025-12-15 18:10:23 by sabo-gla          #+#    #+#             */
/*   Updated: 2025-12-15 18:10:23 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_stack	initialize_empty_stack(void)
{
	t_stack	stack;

	stack.top = NULL;
	stack.size = 0;
	return (stack);
}

t_node	*reserve_memory_for_node(int number)
{
	t_node	*ptr_to_new_node;

	ptr_to_new_node = ft_calloc(1, sizeof(t_node));
	if (!ptr_to_new_node)
		errormsg_exit();
	ptr_to_new_node->value = number;
	ptr_to_new_node->next = NULL;
	return (ptr_to_new_node);
}

void	add_node_to_stackend(t_stack *ptr_stack, t_node *ptr_new_node)
{
	t_node	*wander_ptr_node;

	if (!ptr_stack || !ptr_new_node)
		return ;
	if (ptr_stack->top == NULL)
	{
		ptr_stack->top = ptr_new_node;
		ptr_stack->size++;
		return ;
	}
	wander_ptr_node = ptr_stack->top;
	while (wander_ptr_node->next != NULL)
	{
		wander_ptr_node = wander_ptr_node->next;
	}
	wander_ptr_node->next = ptr_new_node;
	ptr_stack->size++;
}

void	fill_stack_with_split(char **numbers, t_stack *stack)
{
	int		index;
	t_node	*ptr_new_node;

	index = 0;
	while (numbers[index])
	{
		ptr_new_node = reserve_memory_for_node(ft_atoi(numbers[index]));
		add_node_to_stackend(stack, ptr_new_node);
		free(numbers[index]);
		index++;
	}
}

/*
void    parse_args_init_stack(int argc, char **argv)
{
	t_stack stack;
	t_node *ptr_new_node;
	int index;

	stack = initialize_empty_stack();
	index = 1;
	while (index < argc)
	{
		ptr_new_node = reserve_memory_for_node(ft_atoi(argv[index]));
		add_node_to_stackend(&stack, ptr_new_node);
		index++;
	}
	return(stack);
}
*/