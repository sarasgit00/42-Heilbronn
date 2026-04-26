/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025-12-10 01:37:32 by sabo-gla          #+#    #+#             */
/*   Updated: 2025-12-10 01:37:32 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdlib.h>
# include <unistd.h>
# include <limits.h>
# include <stdio.h>
# include "Libft/libft.h"

//structs

typedef struct s_node
{
	int				value;
	struct s_node	*next;
}	t_node;

typedef struct s_stack
{
	t_node	*top;
	int		size;
}	t_stack;

//functions

void	push(t_stack *src_stack, t_stack *dest_stack);
void	swap(t_stack *stack);
void	rotate(t_stack *stack);
void	reverse_rotate(t_stack *stack);
t_stack	initialize_empty_stack(void);
t_node	*reserve_memory_for_node(int value);
void	add_node_to_stackend(t_stack *ptr_stack, t_node *ptr_new_node);
void	fill_stack_with_split(char **numbers, t_stack *stack);
int		is_number(const char *str);
int		is_int_range(long value);
int		has_duplicate(t_stack *stack, int number_to_check);
t_stack	init_stack(int argc, char **argv);
void	errormsg_exit(void);
void	free_stack_nodes(t_stack *stack);
int		is_sorted(t_stack *stack);

// Instructions
void	sa(t_stack *a);
void	sb(t_stack *b);
void	ss(t_stack *a, t_stack *b);
void	pa(t_stack *a, t_stack *b);
void	pb(t_stack *b, t_stack *a);
void	ra(t_stack *a);
void	rb(t_stack *b);
void	rr(t_stack *a, t_stack *b);
void	rra(t_stack *a);
void	rrb(t_stack *b);
void	rrr(t_stack *a, t_stack *b);

// Radix
void	assign_indices(t_stack *stack);
void	radix_sort(t_stack *stack_a, t_stack *stack_b);

#endif