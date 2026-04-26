/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 18:39:57 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/16 19:31:51 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int last_char_occurence)
{
	int	length_or_index;

	length_or_index = ft_strlen(s);
	while (length_or_index >= 0)
	{
		if (s[length_or_index] == (const char)last_char_occurence)
		{
			return ((char *)s + length_or_index);
		}
		length_or_index--;
	}
	return (0);
}
