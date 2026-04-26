/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/22 15:59:26 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/23 16:06:53 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	lenght(long nbr)
{
	int	counter;

	counter = 0;
	if (nbr <= 0)
		counter = 1;
	while (nbr)
	{
		nbr = nbr / 10;
		counter++;
	}
	return (counter);
}

char	*ft_itoa(int n)
{
	char	*conv;
	long	nbr;
	int		nbr_len;

	nbr = n;
	nbr_len = lenght(nbr);
	conv = (char *)malloc(nbr_len + 1);
	if (!conv)
		return (NULL);
	conv[nbr_len--] = '\0';
	if (nbr == 0)
		conv[0] = '0';
	if (nbr < 0)
	{
		conv[0] = '-';
		nbr = -nbr;
	}
	while (nbr)
	{
		conv[nbr_len--] = (nbr % 10) + '0';
		nbr /= 10;
	}
	return (conv);
}
