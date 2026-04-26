/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 15:39:29 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/22 15:58:38 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *big_str, const char *little_str,
		size_t len_to_check)
{
	size_t	index_big;
	size_t	index_lil;

	if (little_str[0] == '\0')
	{
		return ((char *)big_str);
	}
	index_big = 0;
	while (index_big < len_to_check && big_str[index_big] != '\0')
	{
		index_lil = 0;
		while (little_str[index_lil] != '\0' && big_str[index_big
				+ index_lil] == little_str[index_lil] && (index_big
				+ index_lil < len_to_check))
		{
			index_lil++;
		}
		if (little_str[index_lil] == '\0')
		{
			return ((char *)big_str + index_big);
		}
		index_big++;
	}
	return (0);
}
