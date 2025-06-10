# Project : Squaring Even Numbers from 1 to 10.
squ_even=[]
for number in range(1, 11):
    if number % 2 == 0:
        squ_even.append(number ** 2)
        print(squ_even)