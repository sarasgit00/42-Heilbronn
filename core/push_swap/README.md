/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   README.md                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sabo-gla <sabo-gla@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-01-12 18:30:32 by sabo-gla          #+#    #+#             */
/*   Updated: 2026-01-12 18:30:32 by sabo-gla         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

This project has been created as part of the 42 curriculum by <sabo-gla>.

# Description
push_swap is a sorting project that takes a list of integers as arguments and outputs a sequence of stack operations to sort them in ascending order using two stacks, A and B.
The goal is to minimize the number of operations while correctly handling input validation, memory management, and different data sizes.
I used the radix algorithm.
​1. Coordinate Compression: Since Radix Sort depends on indices, the program first "simplifies" the input numbers. It converts messy inputs like [-100, 50, 0] into sorted ranks [0, 2, 1].
2. Bitwise Sorting: It iterates through the bits of the numbers. For each bit (0 to 31):
       If the bit is 0, it pushes the number to Stack B (pb).
       If the bit is 1, it rotates Stack A (ra) to keep the number there.
       After inspecting all numbers for the current bit, everything from Stack B is pushed back to Stack A (`pa`).


# Instructions

The project is compiled with a Makefile producing a push_swap executable:

--Execution--
Running the program with a list of integers:
./push_swap 2 1 3 6 5 8

It also supports a single quoted string of numbers:
./push_swap "2 1 3 6 5 8"
[2]

The parser verifies that every token is a valid number, within int range, and that there are no duplicates; otherwise, the program exits with an error.
​
Algorithm for large datasets
For larger datasets, the program uses an indexed radix-style algorithm based on bitwise passes over stack A, pushing and rotating elements between stacks A and B until they are sorted.
​

# Resources
42 subject PDF for push_swap (official project description and constraints).
Bitwise operations and radix sort overviews (e.g., tutorials on binary representation and LSD radix sort for integers).
General C resources on dynamic memory and linked lists (e.g., documentation on malloc, free, and pointer management).