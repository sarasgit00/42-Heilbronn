/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/11 22:19:48 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/13 22:28:53 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// #include <stdio.h>

char	*ft_strncat(char *dest, char *src, unsigned int nb)
{
	unsigned int	destindex;
	unsigned int	srcindex;

	destindex = 0;
	srcindex = 0;
	while (dest[destindex] != '\0')
	{
		destindex++;
	}
	while (src[srcindex] != '\0' && srcindex < nb)
	{
		dest[destindex + srcindex] = src[srcindex];
		srcindex++;
	}
	dest[destindex + srcindex] = '\0';
	return (dest);
}
// int main ()
// {
//     unsigned int nb;
//     nb = 3;
//     char source[] = "miau\n";
//     char destina[] = "woof";
//     ft_strncat(destina, source, nb);
//     printf ("%s", destina);
// }