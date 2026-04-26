/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 04:51:18 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/16 20:23:44 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdlib.h>
#include <string.h>

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	const unsigned char	*temp_src;
	unsigned char		*temp_dest;
	size_t				index;

	temp_dest = (unsigned char *)dest;
	temp_src = (const unsigned char *)src;
	index = -1;
	if (temp_dest == NULL && temp_src == NULL)
		return (NULL);
	if (temp_dest < temp_src)
	{
		while (++index < n)
			temp_dest[index] = temp_src[index];
	}
	else if (temp_dest > temp_src)
	{
		index = n - 1;
		while ((int)index >= 0)
		{
			temp_dest[index] = temp_src[index];
			index--;
		}
	}
	return (dest);
}

// wenn das Ziel vor der Quelle liegt kann man ganz einfach...
// vorwarts kopieren so wie wir es bei memcopy machen
// ft_memcpy(dest, src, n);

// ruckwarts kopieren, weil umgekehrt