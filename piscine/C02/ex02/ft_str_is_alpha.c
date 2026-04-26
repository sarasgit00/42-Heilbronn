/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_alpha.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/06 16:14:56 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/09 03:10:37 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// #include <stdio.h>

int	ft_str_is_alpha(char *str)
{
	int	index;

	index = 0;
	while (str[index] != '\0')
	{
		if (!((str[index] >= 'A' && str[index] <= 'Z' )
				|| (str[index] >= 'a' && str[index] <= 'z')))
		{
			return (0);
		}
		index++;
	}
	return (1);
}

// int main(){
//     char *does_this_string_have_alphabet;
//     does_this_string_have_alphabet ="4aaaaaASDFGHJ";
//     ft_str_is_alpha(does_this_string_have_alphabet);
//     printf("%d",  ft_str_is_alpha(does_this_string_have_alphabet));

// }