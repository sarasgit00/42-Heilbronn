/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 19:32:53 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/16 20:08:20 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t first_occurence_of_char)
{
	size_t			index;
	unsigned char	*temp_s;

	index = 0;
	temp_s = (unsigned char *)s;
	while (index < first_occurence_of_char)
	{
		if (temp_s[index] == (const unsigned char)c)
		{
			return ((void *)((unsigned char *)temp_s + index));
		}
		index++;
	}
	return (NULL);
}
