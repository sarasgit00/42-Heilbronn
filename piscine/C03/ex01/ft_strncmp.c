/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/10 21:20:44 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/13 22:01:06 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// #include <stdio.h>

int	ft_strncmp(char *s1, char *s2, unsigned int n)
{
	unsigned int	index;

	index = 0;
	while (index < n && (s1[index] != '\0' || s2[index] != '\0'))
	{
		if (s1[index] == s2[index])
		{
			index++;
		}
		else
		{
			return (s1[index] - s2[index]);
		}
	}
	return (0);
}

// int	main(void)
// {   
// 	char	*s1 = "WOOUYYU";
// 	char	*s2 = "WOOUBUU";
// 	printf("%d",  ft_strncmp(s1, s2, 6));
// }
