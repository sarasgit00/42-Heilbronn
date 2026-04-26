/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   hex_low.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-04-10 20:18:25 by sabo-gla          #+#    #+#             */
/*   Updated: 2026-04-10 20:18:25 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	hex_low(unsigned long nbr)
{
	int	hex_low_nbr;

	hex_low_nbr = ft_puthex(nbr, "0123456789abcdef");
	return (hex_low_nbr);
}
