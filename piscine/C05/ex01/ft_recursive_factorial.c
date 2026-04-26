/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/16 22:01:41 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/18 17:12:25 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// #include <stdio.h>

int	ft_recursive_factorial(int nb)
{
	if (nb > 0)
	{
		return (nb * ft_recursive_factorial(nb -1));
	}
	else if (nb == 0)
	{
		return (1);
	}
	else
		return (0);
}

// int main()
// {
//     int nb = 5;
//     printf("%d", ft_recursive_factorial(nb));
// }