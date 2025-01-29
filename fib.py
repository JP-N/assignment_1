# fib.py

# JP Noga
# 1.28.25
# Assignment 1
# Fibonacci - Function to calculate the nth Fibonacci number

# Standard libraries
import functools
import time
from functools import lru_cache

# Math and plotting libraries
import matplotlib.pyplot as plt
import numpy as np

basictimes = []
matrixtimes = []

# Timer decorator nothing fancy
def timer(func):

    @functools.wraps(func)

    def wrapper_timer(*args, **kwargs):

        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        basictimes.append((args[0], elapsed_time))
        print(f"Finished in {elapsed_time:.8f}s: f({args[0]}) -> {value}")
        return value

    return wrapper_timer

# Basic recursive Fibonacci function, not optimzed, big sad :(

@lru_cache(maxsize=None)
@timer
def basic_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return basic_fib(n - 1) + basic_fib(n - 2)

# Matrix exponentiation Fibonacci function, optimized, big happy :)
@lru_cache(maxsize=None)
def matrix_power(mat_tuple, exp):

    mat = np.array(mat_tuple, dtype=object)
    res = np.array([[1, 0], [0, 1]], dtype=object)
    step = 0

    while exp:
        tic = time.perf_counter()
        if exp % 2:
            res = np.matmul(res, mat)
        mat = np.matmul(mat, mat)
        exp //= 2
        toc = time.perf_counter()
        step_time = toc - tic
        matrixtimes.append((step, step_time))
        print(f"Finished Matrix Step {step} in: {step_time:.8f}s")
        step += 1

    return tuple(map(tuple, res))

# Actual function for the Fibonacci number, uses the matrix exponentiation function above
@lru_cache(maxsize=None)
@timer
def fib_matrix(n):
    if n == 0:
        return 0
    F = ((1, 1), (1, 0))
    result = matrix_power(F, n)
    return result[0][1]

# Plotting function for the dual axes graph
def plot_fibonacci_dual_axes(basic_times, matrix_times, title="Fibonacci Methods Comparison"):

    fig = plt.figure(figsize=(20, 8))
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx().twiny()

    basic_iterations, basic_elapsed = zip(*basic_times)
    matrix_iterations, matrix_elapsed = zip(*matrix_times)

    basic_color = 'darkred'
    matrix_color = 'navy'

    basic_line = ax1.plot(basic_iterations, basic_elapsed, color=basic_color,
                          marker='X', mfc='white', markersize=2,
                          label='Basic Recursive')

    matrix_line = ax2.plot(matrix_iterations, matrix_elapsed, color=matrix_color,
                           marker='o', mfc='white', markersize=2,
                           label='Matrix Method')

    ax1.set_xlabel('Fibonacci Number (Basic)', color=basic_color)
    ax1.set_ylabel('Elapsed Time (s)', color=basic_color)
    ax1.tick_params(axis='x', colors=basic_color)
    ax1.tick_params(axis='y', colors=basic_color)

    ax2.set_xlabel('Matrix Step (Matrix)', color=matrix_color)
    ax2.set_ylabel('Elapsed Time (s)', color=matrix_color)
    ax2.tick_params(axis='x', colors=matrix_color)
    ax2.tick_params(axis='y', colors=matrix_color)

    ax1.grid(True, alpha=0.3)

    plt.title(title)

    lines = basic_line + matrix_line
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left')

    return fig, (ax1, ax2)

# Function to plot single graphs
def plot_times(passed_times, graph_scaling, title):

    iterations, elapsed_times = zip(*passed_times)
    plt.title(title)
    plt.plot(iterations, elapsed_times, marker='X', mfc='white', markersize=4)
    plt.xlabel('Fibonacci Number')
    plt.xscale(graph_scaling)
    plt.ylabel('Elapsed Time (s)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":

    # Number of fibonacci numbers to calculate
    fib_numbers = 200

    # Use basic method first, then matrix method
    basic_fib(fib_numbers)
    plot_times(basictimes, "linear", "Basic Recursive Fibonacci")
    fib_matrix(fib_numbers)
    plot_times(matrixtimes, "log", "Matrix Exponentiation Fibonacci")

    # Plot the dual axes graph
    fig, axes = plot_fibonacci_dual_axes(basictimes, matrixtimes)
    plt.show()