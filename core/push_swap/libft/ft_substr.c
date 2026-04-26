/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/18 17:52:34 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/18 19:51:07 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	size_t	index;
	size_t	len_big_str;
	char	*sub_str;

	index = 0;
	len_big_str = ft_strlen(s);
	if (s == NULL)
		return (NULL);
	if (start >= len_big_str)
		return (ft_strdup(""));
	if (len > len_big_str - start)
		len = len_big_str - start;
	sub_str = malloc(sizeof(char) * (len + 1));
	if (sub_str == NULL)
		return (NULL);
	while (index < len)
	{
		sub_str[index] = s[index + start];
		index++;
	}
	sub_str[index] = '\0';
	return (sub_str);
}

// //Explanation :
// S is the original string : "mama-lala-hihi-koko"
// SUBSTRING could be any part of the original string like lala or hihi-koko etc
// START is the starting index where the substring should start in the original
// string and be copied to a pointer that shows to the (beginning of) the substr
// len is the length we want the substring to have