/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   hex_up.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-04-10 20:18:18 by sabo-gla          #+#    #+#             */
/*   Updated: 2026-04-10 20:18:18 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	hex_up(unsigned long nbr)
{
	int	hex_up_nbr;

	hex_up_nbr = ft_puthex(nbr, "0123456789ABCDEF");
	return (hex_up_nbr);
}
