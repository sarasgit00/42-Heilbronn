/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/05 03:36:16 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/05 14:26:55 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strlen(char *str)
{
	int	j;

	j = 0;
	while (*str != '\0')
	{
		str++;
		j++;
	}
	return (j);
}

// int	main(void)
// {
// 	char	*catsound;
// 	int		k;

// 	catsound = "miau";
// 	k = ft_strlen (catsound);
// }
