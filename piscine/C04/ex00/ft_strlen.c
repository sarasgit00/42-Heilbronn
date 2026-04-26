/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/12 23:22:17 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/13 22:42:55 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// #include <stdio.h>

int	ft_strlen(char *str)
{
	int	indexcount;
	int	miau;

	indexcount = 0;
	while (str [indexcount] != '\0')
	{
		indexcount++;
	}
	miau = indexcount;
	return (miau);
}

// int	main(){
// 	char	*stringmiau = "miau";
// 	printf ("%d", ft_strlen (stringmiau));
// }
