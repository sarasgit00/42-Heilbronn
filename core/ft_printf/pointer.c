/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   pointer.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-04-13 16:12:34 by sabo-gla          #+#    #+#             */
/*   Updated: 2026-04-13 16:12:34 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_put_pointer(void *ptr)
{
	unsigned long	hex_nbr;
	int				ox;
	int				hex_p;

	if (!ptr)
		return (ft_putstr("(nil)"));
	hex_nbr = (unsigned long)ptr;
	ox = ft_putstr("0x");
	hex_p = ox + hex_low(hex_nbr);
	return (hex_p);
}
