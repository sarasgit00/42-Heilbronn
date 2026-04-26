*This project has been created as part of the 42 curriculum by sabo-gla.*

# ft_printf

## Description

This project is about making my own printf function in C and implementing it.

The goal is to understand how functions with and unknown amount arguments work (variadic functions).

My function ft_printf works like the original printf, but only for some formats and not all of them.

It supports:

- %c (character)
- %s (string)
- %p (pointer)
- %d / %i (integer)
- %u (unsigned number)
- %x (hex lowercase)
- %X (hex uppercase)
- %% (percent)

---

## Instructions

### Compile

We can compile with the command make and it will create the file libftprintf.a .

### Use

To use it we must include the header: #include "ft_printf.h"

for example:

ft_printf("Hello %s", "miau");

and to compile we execute this command:

cc ft_printf.c libftprintf.a

---

## Algorithm and Data Structure

I read the string one by one.

If I see normal character in the string, I print it.

If I see "%", I check next character and choose correct function.

For numbers I use:

- recursion
- base 10 for decimals
- base 16 for hex

For pointer:

- I print "0x" first
- Then I print the address in hex

Each function returns how many characters it printed.

---

## Resources

- man printf
- google
- 42 subject

### AI usage

I used AI to understand:

- variadic functions and functions like va_list etc.
---
