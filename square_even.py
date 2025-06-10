# print the square of even numbers from 1 to 10
square_even = []
for number in range (1, 11):
    if number % 2 == 0:
        square_even.append(number ** 2)
        print(square_even)
        