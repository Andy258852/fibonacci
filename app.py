#!/usr/bin/env python3
import logging


def set_config():
    logging.basicConfig(format='%(message)s', level=logging.INFO)


def fibonacci(num):
    first = 0
    second = 1
    counter = 1
    while counter < num:
        first, second = second, second + first
        counter += 1
    return first


def main():
    set_config()
    logging.info('Input number of fibonacci sequence:')
    try:
         logging.info(fibonacci(int(input())))
    except ValueError:
         logging.info('Incorrect input')


if __name__== "__main__":
    main()
