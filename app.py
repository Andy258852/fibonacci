#!/usr/bin/env python3
import logging
import math


def fibonacci(n):
    sqrt_5 = math.sqrt(5)
    phi = (sqrt_5 + 1) / 2
    return int(phi ** n / sqrt_5 + 0.5)


def main():
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    num = input("Input number of fibonacci sequence: ")
    if num.isdigit():
        logging.info(fibonacci(int(num)))
    else:
        logging.info("Incorrect input")


if __name__ == "__main__":
    try:
        main()
    except OverflowError:
        logging.info("Too big number")
    except KeyboardInterrupt:
        logging.info("Error")
    except EOFError:
        logging.info("Error")
