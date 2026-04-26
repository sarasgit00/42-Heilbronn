/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-04-10 20:18:12 by sabo-gla          #+#    #+#             */
/*   Updated: 2026-04-10 20:18:12 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	check_format(va_list args, const char format)
{
	if (format == 'c')
		return (ft_putchar(va_arg(args, int)));
	else if (format == 's')
		return (ft_putstr(va_arg(args, char *)));
	else if (format == 'p')
		return (ft_put_pointer(va_arg(args, void *)));
	else if (format == 'd' || format == 'i')
		return (ft_putint(va_arg(args, int)));
	else if (format == 'u')
		return (ft_putdec(va_arg(args, unsigned int)));
	else if (format == 'x')
		return (hex_low(va_arg(args, unsigned int)));
	else if (format == 'X')
		return (hex_up(va_arg(args, unsigned int)));
	else if (format == '%')
		return (ft_putchar('%'));
	return (0);
}

int	ft_printf(const char *format, ...)
{
	int		i;
	int		total_len;
	va_list	args;

	i = 0;
	total_len = 0;
	va_start(args, format);
	while (format[i])
	{
		if (format[i] == '%' && format[i + 1])
		{
			i++;
			total_len += check_format(args, format[i]);
		}
		else
		{
			total_len += ft_putchar(format[i]);
		}
		i++;
	}
	va_end(args);
	return (total_len);
}
