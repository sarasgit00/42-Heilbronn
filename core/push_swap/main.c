/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-01-12 17:24:29 by sabo-gla          #+#    #+#             */
/*   Updated: 2026-01-12 17:24:29 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	main(int argc, char **argv)
{
	t_stack	a;
	t_stack	b;

	a = init_stack(argc, argv);
	b = initialize_empty_stack();
	if (a.size > 1)
	{
		assign_indices(&a);
		if (!is_sorted(&a))
			radix_sort(&a, &b);
	}
	free_stack_nodes(&a);
	free_stack_nodes(&b);
	return (0);
}
