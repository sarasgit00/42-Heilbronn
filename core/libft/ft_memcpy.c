/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 04:21:31 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/19 22:56:16 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	size_t	index;

	index = 0;
	if (dest == NULL && src == NULL)
		return (NULL);
	while (index < n)
	{
		((unsigned char *)dest)[index] = ((const unsigned char *)src)[index];
		index++;
	}
	return (dest);
}
// int main()
// {
// 	void *destina = "hey oh no was";
// 	const void *src = "hahahahaha";

// 	ft_memcpy(destina, src, sizeof(char) * 5);

// 	printf("%s", destina);
// }