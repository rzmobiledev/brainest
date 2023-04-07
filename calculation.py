"""
Exercise 1: Write a program which repeatedly reads numbers until the
user enters `done`. Once `done` is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333

from statistics import mean
functions to be used: sum(), len(), mean()

if you did the first part, try to return the largest and smallest values as well.
If you did the tasks, please feel free to leave.
"""
from statistics import mean


def result(number: list[int]):
    sum_all_numbers = sum(all_numbers)
    len_all_numbers = len(all_numbers)
    mean_all_numbers = mean(all_numbers)

    return tuple([sum_all_numbers, len_all_numbers, mean_all_numbers])


all_numbers = list()

while True:
    done: str = "done"
    input_num = input("Enter a number: ")

    try:
        number = int(input_num)
        all_numbers.append(number)
    except Exception:
        if input_num == done or input_num == done.title():
            break
        print("Invalid input")
        continue

sum_num, len_num, mean_num = result(all_numbers)

print("{} {} {}".format(sum_num, len_num, mean_num))
print("You exited the program")