/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 22:22:20 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/22 15:42:06 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	unsigned int	i;
	char			*memoria;
	size_t			length;

	length = ft_strlen(s);
	i = 0;
	memoria = malloc(length + 1);
	if (memoria == 0)
		return (0);
	while (i < length)
	{
		memoria[i] = (*f)(i, s[i]);
		i++;
	}
	memoria[i] = '\0';
	return (memoria);
}
