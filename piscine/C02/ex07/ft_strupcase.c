/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strupcase.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/07 20:17:53 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/09 03:04:01 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// #include <stdio.h>

char	*ft_strupcase(char *str)
{
	int	index;

	index = 0;
	while (str[index] != '\0')
	{
		if (str[index] >= 'a' && str[index] <= 'z')
		{
			str[index] = str[index] -32;
		}
		index++;
	}
	return (str);
}

// int main(){
//     char  teststringarray[] = "asdas"; //because im modifying something
//     char *stringi = teststringarray; 
//     ft_strupcase(stringi);
//     printf("%s", stringi);
// }