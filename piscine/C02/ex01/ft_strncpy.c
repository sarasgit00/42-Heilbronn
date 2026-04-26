/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/06 02:10:13 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/08/09 03:10:45 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// #include <stdio.h>

char	*ft_strncpy(char *dest, char *src, unsigned int n)
{
	unsigned int	index;

	index = 0;
	while (index < n && src[index] != '\0')
	{
		dest[index] = src[index];
		index++;
	}
	while (index < n)
	{
		dest[index] = '\0';
		index++;
	}
	return (dest);
}

// int    main(void)
// {
//     char    src[] = "Test";
//     char    dest[10];

//     printf("Copying 'Test' with n=7\n");
//     ft_strncpy(dest, src, 7);
//     printf("Result: ");
//     for (int i=0; i<7; i++)
//     {
//         if(dest[i] == '\0')
//             printf("\\0");
//         else
//             printf("%c", dest[i]);
//     }
//     printf("\n");
//     return (0);
// }