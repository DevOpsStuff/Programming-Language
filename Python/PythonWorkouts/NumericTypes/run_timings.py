#!/usr/bin/env python

def run_timing():
    """
    Asks the user repeatedly for numberic input. Prints the average time and number of runs
    """

    num_of_runs = 0
    total_time = 0

    while True:
        one_run = input('Enter 10 Km run time: ')

        if not one_run:
            break

        num_of_runs += 1
        total_time += float(one_run)

    average_time = total_time / num_of_runs

    print(f'Average of {average_time}, over {num_of_runs} runs')

run_timing()

