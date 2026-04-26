/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_params.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/19 21:57:17 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/19 23:11:44 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(int argc, char *argv[])
{
	char	*pointer;
	int		index;

	index = argc - 1;
	while (index > 0)
	{
		pointer = argv[index];
		while (*pointer)
		{
			write(1, pointer, 1);
			pointer++;
		}
		write(1, "\n", 1);
		index--;
	}
	return (0);
}
