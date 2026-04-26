/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/14 23:24:10 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/15 23:19:12 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_atoi(char *str)
{
	int	index;
	int	outcome;
	int	sign;

	outcome = 0;
	index = 0;
	sign = 1;
	while (str[index] == ' ' || (str[index] <= '\r' && str[index] >= '\t'))
	{
		index++;
	}
	while (str[index] == '-' || str[index] == '+')
	{
		if (str[index] == '-')
		{
			sign = sign * -1;
		}
		index++;
	}
	while (str[index] >= '0' && str[index] <= '9')
	{
		outcome = outcome * 10 + (str[index] - '0');
		index++;
	}
	return (outcome * sign);
}
