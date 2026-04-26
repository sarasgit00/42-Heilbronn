/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 16:22:50 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/25 03:10:41 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memset(void *str_array, int replacement, size_t amount)
{
	unsigned char	*replacement_of_str_array;
	size_t			index;

	index = 0;
	replacement_of_str_array = (unsigned char *)str_array;
	while (index < amount)
	{
		replacement_of_str_array[index] = (unsigned char)replacement;
		index++;
	}
	return (replacement_of_str_array);
}

// void	*ft_memset(void *str_array, int replacement, size_t amount)
// {
// 	unsigned char	*replacement_of_str_array;
// 	size_t			index;

// 	// its gonna be the new index in the middle of the string where we wanna
//  start replacing the original strig with our replacement.
// 	index = 0;
// 	// we set the new in the middle of the string index to zero
// 	replacement_of_str_array = (unsigned char *)str_array;
// 	// we cast str_array to unsigned char because its initially void
//  in the original memset function
// 	while (index < amount)
// 	{
// 		replacement_of_str_array[index] = (unsigned char)replacement;
// 		// the replacement is happening here
// 		index++;
// 	}
// 	return (replacement_of_str_array);
// }
