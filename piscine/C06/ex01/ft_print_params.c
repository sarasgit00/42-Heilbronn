/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_params.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/19 04:17:10 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/19 23:10:56 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(int argc, char *argv[])
{
	char	*ptr;
	int		index;

	index = 1;
	while (index < argc)
	{
		ptr = argv[index];
		while (*ptr)
		{
			write(1, ptr, 1);
			ptr++;
		}
		index++;
		write(1, "\n", 1);
	}
	return (0);
}
