#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_integers(numbers):
    return [int(number) for number in numbers.split()]
def split_list_even_odd(numbers):
    odd_numbers = [number for number in numbers if number % 2 == 1]
    even_numbers = [number for number in numbers if number % 2 == 0]
    return odd_numbers, even_numbers
numbers = input("Список чисел: ")
numbers = get_integers(numbers)
print("Нечетные числа{}".format(split_list_even_odd(numbers)[0]))
print("Чётные числа  {}".format(split_list_even_odd(numbers)[1]))