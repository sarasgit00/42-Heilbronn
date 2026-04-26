/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 21:29:18 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/17 21:45:17 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *src)
{
	size_t	index;
	char	*pointer_to_dest;

	index = 0;
	while (src[index] != '\0')
		index++;
	pointer_to_dest = (char *) malloc(sizeof(char) * index + 1);
	if (pointer_to_dest == NULL)
		return (NULL);
	index = 0;
	while (src[index] != '\0')
	{
		pointer_to_dest[index] = src[index];
		index++;
	}
	pointer_to_dest[index] = '\0';
	return (pointer_to_dest);
}
