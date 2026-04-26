/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/18 16:33:56 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/18 17:44:53 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t amount, size_t size)
{
	size_t	index;
	char	*ptr_to_emptify;

	index = 0;
	ptr_to_emptify = (void *)malloc(amount * size);
	if (ptr_to_emptify == NULL)
	{
		return (NULL);
	}
	while (index < amount * size)
	{
		ptr_to_emptify[index] = 0;
		index++;
	}
	return (ptr_to_emptify);
}
