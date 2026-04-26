/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/18 19:45:34 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/19 17:16:04 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	size_t	index;
	size_t	len_s1_s2;
	char	*new_str;

	index = 0;
	len_s1_s2 = ft_strlen(s1) + ft_strlen(s2);
	if (s1 == NULL || s2 == NULL)
		return (NULL);
	new_str = malloc(sizeof(char) * (len_s1_s2 + 1));
	if (new_str == NULL)
		return (NULL);
	while (index < ft_strlen(s1))
	{
		new_str[index] = s1[index];
		index++;
	}
	while (index < len_s1_s2)
	{
		new_str[index] = s2[index - ft_strlen(s1)];
		index++;
	}
	new_str[index] = '\0';
	return (new_str);
}
