/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 00:14:34 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/16 20:08:42 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

// void	ft_bzero(void *str_arr, size_t amount_of_bytes)
// {
// 	while (amount_of_bytes--)
// 	{
// 		((unsigned char *)str_arr)[amount_of_bytes] = NULL;
// 	}
// }
void	ft_bzero(void *str_arr, size_t amount)
{
	unsigned char	*replacing_str_arr;
	size_t			index;

	replacing_str_arr = (char unsigned *)str_arr;
	index = 0;
	while (index < amount)
	{
		replacing_str_arr[index] = '\0';
		index++;
	}
}

// int main()
// {
//     char stringy[30]= "miauwedoony";

//     ft_bzero(stringy, sizeof(char) * 5);

//     // "00000edoony"
//     printf("%c", stringy[7]);
// }