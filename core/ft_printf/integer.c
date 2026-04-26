/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   integer.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-04-10 20:18:21 by sabo-gla          #+#    #+#             */
/*   Updated: 2026-04-10 20:18:21 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putint(int nbr)
{
	int	nbr_len;

	nbr_len = 0;
	if (nbr == -2147483648)
	{
		write(1, "-2147483648", 11);
		return (11);
	}
	if (nbr < 0)
	{
		nbr_len = nbr_len + ft_putchar('-');
		nbr *= -1;
	}
	nbr_len = nbr_len + ft_putnbr(nbr);
	return (nbr_len);
}
