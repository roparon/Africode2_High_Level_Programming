#long list comprehension method

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square_of_even_numbers = []
# for number in numbers:
#     if number % 2 ==0:
#         square_of_even_numbers.append(number ** 2)
# print(square_of_even_numbers)

#shorter list comprehension method
square_of_even_numbers =[numbers**2 for numbers in numbers if numbers % 2 == 0]
print(square_of_even_numbers)