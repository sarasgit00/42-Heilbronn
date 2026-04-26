/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/10 17:21:04 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/13 22:28:46 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// #include <stdio.h>

int	ft_strcmp(char *s1, char *s2)
{
	int	index;

	index = 0;
	while (s1[index] != '\0' || s2[index] != '\0')
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

/*int	main(void)
{
	char	*s1 = "WIeF";
	char	*s2 = "WOO";
	printf("%d",  ft_strcmp(s1, s2));
}*/
