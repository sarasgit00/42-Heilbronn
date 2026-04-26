# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sabo-gla <sabo-gla@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/14 22:38:12 by sabo-gla          #+#    #+#              #
#    Updated: 2025/10/24 21:39:20 by sabo-gla         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libft.a

CC = cc

CFLAGS = -Werror -Wextra -Wall

SRC = ft_bzero.c \
ft_isalnum.c \
ft_isalpha.c \
ft_isascii.c \
ft_isdigit.c \
ft_isprint.c \
ft_memcpy.c \
ft_memmove.c \
ft_memset.c \
ft_strlcat.c \
ft_strlcpy.c \
ft_strlen.c \
ft_tolower.c \
ft_toupper.c \
ft_strchr.c \
ft_strrchr.c \
ft_strncmp.c \
ft_memchr.c \
ft_memcmp.c \
ft_strnstr.c \
ft_atoi.c \
ft_strdup.c \
ft_calloc.c \
ft_substr.c \
ft_strjoin.c \
ft_strtrim.c \
ft_strmapi.c \
ft_itoa.c \
ft_striteri.c \
ft_putstr_fd.c \
ft_putchar_fd.c \
ft_split.c \
ft_putendl_fd.c \
ft_putnbr_fd.c



OBJ = $(SRC:.c=.o)

$(NAME) : $(OBJ)
	ar rcs $(NAME) $(OBJ)

all: $(NAME)

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re