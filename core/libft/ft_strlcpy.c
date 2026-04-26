/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 18:01:15 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/24 20:59:06 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t	index;
	size_t	length_of_sauce;

	index = 0;
	length_of_sauce = ft_strlen(src);
	if (size > 0)
	{
		while (index < size - 1 && src[index] != '\0')
		{
			dst[index] = src[index];
			index++;
		}
		dst[index] = '\0';
	}
	return (length_of_sauce);
}
