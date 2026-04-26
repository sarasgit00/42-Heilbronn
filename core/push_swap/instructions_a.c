/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   instructions_a.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-01-07 20:03:49 by sabo-gla          #+#    #+#             */
/*   Updated: 2026-01-07 20:03:49 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	sa(t_stack *a)
{
	swap(a);
	ft_putstr_fd("sa\n", 1);
}

void	ra(t_stack *a)
{
	rotate(a);
	ft_putstr_fd("ra\n", 1);
}

void	rra(t_stack *a)
{
	reverse_rotate(a);
	ft_putstr_fd("rra\n", 1);
}

void	pa(t_stack *a, t_stack *b)
{
	push(b, a);
	ft_putstr_fd("pa\n", 1);
}
