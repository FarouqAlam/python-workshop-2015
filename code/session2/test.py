# -*- coding: utf-8 -*-
"""
Calculate the avergae of numbers.
Created on Tue Jun  9 10:25:16 2015

@author: farouq
"""

def average(nums):
    n = len(nums)
    return sum(nums) * 1.0 / n

def main(options):
    my_nums = options.nums
    my_ints = []
    for i in my_nums:
        my_ints.append(float(i))
    my_avg = average(my_ints)
    print 'Average = ' + str(my_avg)
    print 'The average of {} is {}'.format(my_nums, my_avg)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('nums', nargs = '*', help = "A list of numbers.")
    options = parser.parse_args()
    main(options)
