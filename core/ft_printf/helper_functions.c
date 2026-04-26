/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   helper_functions.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-04-10 20:18:03 by sabo-gla          #+#    #+#             */
/*   Updated: 2026-04-10 20:18:03 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_strlen(char *str) // Because orignial prinft returns len
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

int	ft_putchar(char c)
{
	write(1, &c, 1);
	return (1);
}

int	ft_putstr(char *text)
{
	int	i;

	i = 0;
	if (!text)
		text = "(null)";
	while (text[i])
	{
		ft_putchar(text[i]);
		i++;
	}
	return (i);
}

int	ft_putnbr(int nbr)
{
	int	nbr_len;

	nbr_len = 0;
	if (nbr >= 10)
		nbr_len = nbr_len + ft_putnbr(nbr / 10);
	nbr_len = nbr_len + ft_putchar("0123456789"[nbr % 10]);
	return (nbr_len);
}

int	ft_puthex(unsigned long nbr, const char *base)
{
	int	nbr_len;

	nbr_len = 0;
	if (nbr >= 16)
		nbr_len = nbr_len + ft_puthex(nbr / 16, base);
	nbr_len = nbr_len + ft_putchar(base[nbr % 16]);
	return (nbr_len);
}
