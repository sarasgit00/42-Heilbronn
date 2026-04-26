/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 20:12:40 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/24 20:55:11 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	ft_seperator_counter(char const *str, char sep)
{
	int	index;
	int	words;

	index = 0;
	words = 0;
	if (str == 0)
		return (0);
	while (str[index])
	{
		while (str[index] && str[index] == sep)
		{
			index++;
		}
		if (str[index])
		{
			words++;
			while (str[index] != sep && str[index])
			{
				index++;
			}
		}
	}
	return (words);
}

static char	**save_ram(char **reserved_mem)
{
	int	index;

	index = 0;
	while (reserved_mem[index])
	{
		free(reserved_mem[index++]);
	}
	free(reserved_mem);
	return (NULL);
}

static char	**core_function(char **split, char const *s, char c)
{
	int	start;
	int	end;
	int	j;

	start = 0;
	end = 0;
	j = 0;
	while (s[end])
	{
		while (s[end] && s[end] == c)
			end++;
		start = end;
		while (s[end] && s[end] != c)
			end++;
		if (end > start)
		{
			split[j] = ft_substr(s, start, end - start);
			if (!split[j])
				return (save_ram(split));
			j++;
		}
	}
	split[j] = NULL;
	return (split);
}

char	**ft_split(char const *s, char c)
{
	char	**memory;

	if (!s)
	{
		return (NULL);
	}
	memory = (char **)malloc((ft_seperator_counter(s, c) + 1) * sizeof(char *));
	if (!memory)
	{
		return (NULL);
	}
	return (core_function(memory, s, c));
}
