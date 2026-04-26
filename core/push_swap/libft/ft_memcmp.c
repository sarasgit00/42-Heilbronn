/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 20:36:44 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/16 20:53:11 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	size_t				index;
	unsigned const char	*source1;
	unsigned const char	*source2;

	index = 0;
	source1 = (unsigned const char *)s1;
	source2 = (unsigned const char *)s2;
	while (index < n)
	{
		if (source1[index] != source2[index])
		{
			return (source1[index] - source2[index]);
		}
		index++;
	}
	return (0);
}

// #include "libft.h"

// int	ft_strncmp(const char *s1, const char *s2, size_t n)
// {
// 	size_t	index;

// 	if (n == 0)
// 	{
// 		return (0);
// 	}
// 	index = 0;
// 	while (index < n)
// 	{
// 		if ((unsigned char)s1[index] != (unsigned char)s2[index]
// 			|| s1[index] == '\0')
// 		{
// 			return ((unsigned char)s1[index] - (unsigned char)s2[index]);
// 		}
// 		index++;
// 	}
// 	return (0);
// }
