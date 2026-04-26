/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 15:09:46 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/17 22:49:37 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strchr(const char *s, int first_char_occurence)
{
	int	index;
	int	length;

	index = 0;
	length = ft_strlen(s);
	while (index <= length)
	{
		if (s[index] == (const char)first_char_occurence)
		{
			return ((char *)(s + index));
		}
		index++;
	}
	return (0);
}
