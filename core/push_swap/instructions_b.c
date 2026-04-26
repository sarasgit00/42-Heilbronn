/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   instructions_b.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-01-07 20:05:05 by sabo-gla          #+#    #+#             */
/*   Updated: 2026-01-07 20:05:05 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	sb(t_stack *b)
{
	swap(b);
	ft_putstr_fd("sb\n", 1);
}

void	rb(t_stack *b)
{
	rotate(b);
	ft_putstr_fd("rb\n", 1);
}

void	rrb(t_stack *b)
{
	reverse_rotate(b);
	ft_putstr_fd("rrb\n", 1);
}

void	pb(t_stack *b, t_stack *a)
{
	push(a, b);
	ft_putstr_fd("pb\n", 1);
}
