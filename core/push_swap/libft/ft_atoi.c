/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 19:15:26 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/25 02:32:59 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_atoi(const char *str)
{
	int	index;
	int	outcome;
	int	sign;

	outcome = 0;
	index = 0;
	sign = 1;
	while ((str[index] >= '\t' && str[index] <= '\r') || str[index] == ' ')
	{
		index++;
	}
	if (str[index] == '-' || str[index] == '+')
	{
		if (str[index] == '-')
		{
			sign = sign * -1;
		}
		index++;
	}
	while (str[index] >= '0' && str[index] <= '9')
	{
		outcome = (outcome * 10) + (str[index] - '0');
		index++;
	}
	return (outcome * sign);
}
