/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025-12-17 18:49:43 by sabo-gla          #+#    #+#             */
/*   Updated: 2025-12-17 18:49:43 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static long	ft_atol(const char *str);

static void	parse_arg_with_split(char *arg, t_stack *stack)
{
	char	**numbers;
	int		index;
	long	value;

	numbers = ft_split(arg, ' ');
	if (!numbers)
		errormsg_exit();
	index = 0;
	while (numbers[index])
	{
		if (!is_number(numbers[index]))
			errormsg_exit();
		value = ft_atol(numbers[index]);
		if (!is_int_range(value))
			errormsg_exit();
		if (has_duplicate(stack, (int)value))
			errormsg_exit();
		add_node_to_stackend(stack, reserve_memory_for_node((int)value));
		free(numbers[index]);
		index++;
	}
	free(numbers);
}

static long	ft_atol(const char *str)
{
	long	outcome;
	int		sign;
	int		index;

	outcome = 0;
	index = 0;
	sign = 1;
	while ((str[index] >= 9 && str[index] <= 13) || str[index] == 32)
		index++;
	if (str[index] == '-' || str[index] == '+')
	{
		if (str[index] == '-')
			sign = -1;
		index++;
	}
	while (str[index] >= '0' && str[index] <= '9')
	{
		outcome = (outcome * 10) + (str[index] - '0');
		index++;
	}
	return (outcome * sign);
}

static void	parse_many_args(int argc, char **argv, t_stack *stack)
{
	int		index;
	long	value;

	index = 1;
	while (index < argc)
	{
		if (!is_number(argv[index]))
			errormsg_exit();
		value = ft_atol(argv[index]);
		if (!is_int_range(value))
			errormsg_exit();
		if (has_duplicate(stack, ((int)value)))
			errormsg_exit();
		add_node_to_stackend(stack, reserve_memory_for_node((int)value));
		index++;
	}
}

t_stack	init_stack(int argc, char **argv)
{
	t_stack	stack;

	stack = initialize_empty_stack();
	if (argc <= 1)
		return (stack);
	if (argc == 2)
		parse_arg_with_split(argv[1], &stack);
	else
		parse_many_args(argc, argv, &stack);
	return (stack);
}
