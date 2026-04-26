/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/02 16:30:50 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/03 15:08:04 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char a, char b, char c)
{
	write (1, &a, 1);
	write (1, &b, 1);
	write (1, &c, 1);
	if (a < '7')
	{
		write (1, ", ", 2);
	}
}

void	ft_print_comb(void)
{
	char	zero;
	char	one;
	char	two;

	zero = '0';
	while (zero <= '7')
	{
		one = zero + 1;
		while (one <= '8')
		{
			two = one + 1;
			while (two <= '9')
			{
				ft_putchar(zero, one, two);
				two++;
			}
			one++;
		}
		zero++;
	}
}

/*int	main(void)
{
	ft_print_comb();
}*/
