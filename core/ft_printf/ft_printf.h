/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-04-10 19:04:52 by sabo-gla          #+#    #+#             */
/*   Updated: 2026-04-10 19:04:52 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>

int	ft_putdec(unsigned int nbr);
int	ft_strlen(char *str);
int	ft_putchar(char c);
int	ft_putstr(char *text);
int	ft_putnbr(int nbr);
int	ft_puthex(unsigned long nbr, const char *base);
int	hex_low(unsigned long nbr);
int	hex_up(unsigned long nbr);
int	ft_putint(int nbr);
int	ft_put_pointer(void *ptr);
int	ft_printf(const char *format, ...);

#endif