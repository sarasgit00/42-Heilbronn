/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/14 16:20:48 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/15 00:24:26 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	negative(int n)
{
	int		index;
	char	negative_numbers[10];

	if (n == -2147483648)
		write(1, "-2147483648", 11);
	else
	{
		index = 0;
		n = n * -1;
		while (n > 0)
		{
			negative_numbers[index] = (n % 10) + '0';
			n /= 10;
			index++;
		}
		write(1, "-", 1);
		index--;
		while (index >= 0)
		{
			write(1, &negative_numbers[index], 1);
			index--;
		}
	}
}

void	position(int n)
{
	int		index;
	char	positive_numbers[10];

	index = 0;
	while (n > 0)
	{
		positive_numbers[index] = (n % 10) + '0';
		n /= 10;
		index++;
	}
	index--;
	while (index >= 0)
	{
		write(1, &positive_numbers[index], 1);
		index--;
	}
}

void	ft_putnbr(int nb)
{
	if (nb == 0)
		write(1, "0", 1);
	else if (nb > 0)
		position(nb);
	else
		negative(nb);
}

/*int main()
{
    ft_putnbr(5435454);
}*/