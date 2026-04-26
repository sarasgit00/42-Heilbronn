/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcat.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/11 01:36:20 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/12 19:36:04 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strcat(char *dest, char *src)
{
	int	index_for_dest;
	int	index_for_src;

	index_for_dest = 0;
	index_for_src = 0;
	while (dest[index_for_dest] != '\0')
	{
		index_for_dest++;
	}
	while (src[index_for_src] != '\0' )
	{
		dest[index_for_dest] = src[index_for_src];
		index_for_dest ++;
		index_for_src ++;
	}
	dest[index_for_dest] = '\0';
	return (dest);
}
// concatinate, to add a string to another without 
// overwriting it? here were adding the source to the 
// (already) existing string.
