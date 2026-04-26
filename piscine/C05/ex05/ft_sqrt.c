/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sqrt.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/18 02:06:14 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/18 17:31:35 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// #include <stdio.h>

int	ft_sqrt(int nb)
{
	int	counter;

	counter = 1;
	if (nb <= 0)
	{
		return (0);
	}
	if (nb == 1)
	{
		return (1);
	}
	while (counter * counter <= nb)
	{
		if (counter * counter == nb)
		{
			return (counter);
		}
		counter++;
	}
	return (0);
}

// int main(){
//     int nb = 2;
//     printf("%d", ft_sqrt(nb));
// }