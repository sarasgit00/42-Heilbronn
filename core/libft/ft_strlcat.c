/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 20:22:28 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/16 17:53:51 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src,
		size_t size_how_much_dest_can_hold)
{
	size_t	index;
	size_t	sauce_length;
	size_t	desti_length;

	index = 0;
	sauce_length = ft_strlen(src);
	if (size_how_much_dest_can_hold == 0)
	{
		return (sauce_length);
	}
	desti_length = ft_strlen(dst);
	if (size_how_much_dest_can_hold <= desti_length)
	{
		return (sauce_length + size_how_much_dest_can_hold);
	}
	while (index < size_how_much_dest_can_hold - 1 - desti_length && src[index])
	{
		dst[index + desti_length] = src[index];
		index++;
	}
	dst[desti_length + index] = '\0';
	return (desti_length + sauce_length);
}
