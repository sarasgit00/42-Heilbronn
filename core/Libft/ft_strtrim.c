/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 17:16:25 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/24 20:58:17 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	size_t	start_i;
	size_t	end_i;
	size_t	new_len;
	char	*trimed_str;

	if (s1 == NULL || set == NULL)
		return (NULL);
	start_i = 0;
	while (s1[start_i] != '\0' && ft_strchr(set, s1[start_i]) != NULL)
		start_i++;
	end_i = ft_strlen(s1);
	if (end_i > 0)
		while (s1[end_i - 1] && ft_strchr(set, s1[end_i - 1]) != NULL)
			end_i--;
	new_len = end_i - start_i;
	trimed_str = ft_substr(s1, start_i, new_len);
	return (trimed_str);
}

// In C gibt es eine Regel:
// Wenn du einen char an eine Funktion übergibst, die einen int erwartet,
// wird der char automatisch in einen int konvertiert (promoted).
// Das nennt man integer promotion.
// Das passiert still und automatisch — du musst dich nicht drum kümmern.

// „Ist das aktuelle Zeichen von s1 im Set enthalten?“
