/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_toupper.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 21:04:09 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/17 15:44:21 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_toupper(int lowercase)
{
	int	conv_uppercase;

	if (lowercase >= 97 && lowercase <= 122)
	{
		conv_uppercase = lowercase - 32;
		return (conv_uppercase);
	}
	return (lowercase);
}
