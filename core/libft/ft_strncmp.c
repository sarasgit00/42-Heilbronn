/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 19:33:48 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/25 03:10:29 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	size_t	index;

	if (n == 0)
	{
		return (0);
	}
	index = 0;
	while (index < n)
	{
		if ((unsigned char)s1[index] != (unsigned char)s2[index]
			|| s1[index] == '\0')
		{
			return ((unsigned char)s1[index] - (unsigned char)s2[index]);
		}
		index++;
	}
	return (0);
}
