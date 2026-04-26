/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 15:42:46 by sabo-gla          #+#    #+#             */
/*   Updated: 2025/10/25 04:07:44 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
# define LIBFT_H

# include <stddef.h>
# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>

int		ft_isalpha(int alpha);
int		ft_isdigit(int digit);
int		ft_isascii(int ascii);
int		ft_isprint(int printable);
void	*ft_memset(void *str_array, int replacement, size_t amount);
void	ft_bzero(void *str_arr, size_t amount_of_bytes);
void	*ft_memcpy(void *dest, const void *src, size_t n); // obacht
size_t	ft_strlen(const char *string);
int		ft_isalnum(int alnum);
size_t	ft_strlcpy(char *dst, const char *src, size_t size);
size_t	ft_strlcat(char *dst, const char *src, size_t size);
int		ft_toupper(int lowercase);
int		ft_tolower(int uppercase);
void	*ft_memmove(void *dest, const void *src, size_t n);
char	*ft_strchr(const char *s, int first_char_occurence);
char	*ft_strrchr(const char *s, int last_char_occurence);
int		ft_strncmp(const char *s1, const char *s2, size_t n);
void	*ft_memchr(const void *s, int c, size_t n);
int		ft_memcmp(const void *s1, const void *s2, size_t n);
char	*ft_strnstr(const char *big_str, const char *little_str,
			size_t len_to_check);
int		ft_atoi(const char *str);
char	*ft_strdup(const char *src);
void	*ft_calloc(size_t amount, size_t size);
char	*ft_substr(char const *s, unsigned int start, size_t len);
char	*ft_strjoin(char const *s1, char const *s2);
char	*ft_strtrim(char const *s1, char const *set);
char	*ft_strmapi(char const *s, char (*f)(unsigned int, char));
char	*ft_itoa(int n);
void	ft_striteri(char *s, void (*f)(unsigned int, char *));
void	ft_putchar_fd(char c, int fd);
void	ft_putstr_fd(char *s, int fd);
char	**ft_split(char const *s, char c);
void	ft_putendl_fd(char *s, int fd);
void	ft_putnbr_fd(int n, int fd);

#endif