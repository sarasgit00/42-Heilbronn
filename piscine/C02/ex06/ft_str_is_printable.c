/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_printable.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/07 18:02:22 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/09 03:09:37 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// #include <stdio.h>

int	ft_str_is_printable(char *str)
{
	int	index;

	index = 0;
	while (str[index])
	{
		if (str[index] < 32 || str[index] > 126)
			return (0);
		index++;
	}
	return (1);
}

// int main(){
//     char *printablecharacters = "\n" ;
//     printf("%d", ft_str_is_printable(printablecharacters));
// }
