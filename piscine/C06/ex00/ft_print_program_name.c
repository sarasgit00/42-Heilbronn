/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_program_name.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/19 02:47:09 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/19 23:13:23 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// #include <unistd.h>

// char ft_print_program_name(char *str)
// {
//     int index;

//     index = 0;
//     while (*str)
//     {
//         str++;
//         index++;
//     }
//     return(index);
// }

// int main(int argc, char *argv[])
// {
//     if(argc == 0)
//     {
//         write(1, argv[argc -1], ft_print_program_name(argv[argc -1]));
//     }
//     else
//         write(1, argv[0], ft_print_program_name(argv[0]));
//     write(1, "\n", 1);
// }

#include <unistd.h> 

int	main(int argc, char *argv[])
{
	char	*ptr;

	if (argc)
	{
		ptr = argv[0];
		while (*ptr != '\0')
		{
			write (1, ptr, 1);
			ptr++;
		}
		write(1, "\n", 1);
	}
	return (0);
}
