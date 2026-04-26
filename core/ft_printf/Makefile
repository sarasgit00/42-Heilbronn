NAME  := libftprintf.a
CC 	:= cc
CFLAGS := -Wall -Wextra -Werror
SRC := ft_printf.c decimal.c helper_functions.c hex_low.c hex_up.c integer.c pointer.c

OBJ := $(SRC:.c=.o)

$(NAME): $(OBJ)
	ar crs $(NAME) $(OBJ)

all : $(NAME)

clean :
	rm -f $(OBJ)

fclean : clean
	rm -f $(NAME)

re : fclean all

.PHONY: all clean fclean re
