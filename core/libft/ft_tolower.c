/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_tolower.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 21:30:21 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/17 15:44:37 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_tolower(int uppercase)
{
	int	conv_lowercase;

	if (uppercase >= 65 && uppercase <= 90)
	{
		conv_lowercase = uppercase + 32;
		return (conv_lowercase);
	}
	return (uppercase);
}
