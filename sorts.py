"""
Colin Reilly
Homework 01
Analysis of Algorithms
Rochester Institute of Technol1ogy
1/27/18

Sorting Function Analysis
    MergeSort, InsertionSort, BucketSort
"""

# upercase constants warning
# pylint: disable=C0103

import math
import time
import numpy as np

# functions to get random number data
def get_u100():     return np.random.uniform(0, 1, 100).tolist()
def get_u1000():    return np.random.uniform(0, 1, 1000).tolist()
def get_u10000():   return np.random.uniform(0, 1, 10000).tolist()
def get_u100000():  return np.random.uniform(0, 1, 100000).tolist()
def get_u1000000(): return np.random.uniform(0, 1, 1000000).tolist()

def get_n100():     return np.random.normal(0.5, 1/10000, 100).tolist()
def get_n1000():    return np.random.normal(0.5, 1/10000, 1000).tolist()
def get_n10000():   return np.random.normal(0.5, 1/10000, 10000).tolist()
def get_n100000():  return np.random.normal(0.5, 1/10000, 100000).tolist()
def get_n1000000(): return np.random.normal(0.5, 1/10000, 1000000).tolist()

def insertion_sort(data):
    """ Sort @data using the Insertion Sort method
        and return the time it took to do so
    """

    start_time = time.time()

    i = 1

    # go through the data
    while i < len(data):
        j = i
        # move the next element down the sorted array
        # until we find it's proper sorted place
        while j > 0 and data[j - 1] > data[j]:
            a = data[j]
            b = data[j - 1]
            data[j] = b
            data[j - 1] = a
            j = j - 1
        i = i + 1

    # return the time it took to sort the data
    return time.time() - start_time

def bucket_sort(data):
    """ Sort @data using the Bucket Sort method
        Assumes values in 0 <= x <= 1
    """

    # initialize 10 buckets
    buckets = []
    for i in range(0, 10):
        buckets.append([])

    start_time = time.time()

    # put elements into their proper buckets
    for d in data:
        buckets[math.floor(d * 10)].append(d)

    # sort each bucket using insertion sort
    for i in range(0, 10):
        insertion_sort(buckets[i])

    # concatenate the buckets into one list
    result = []
    for b in buckets:
        for bb in b:
            result.append(bb)
    
    return time.time() - start_time

def merge(a, b):
    """ Merge two arrays """

    c = []
    while a and b:
        # looking at the first element in a and b
        # pick the smaller of the two
        # and add it to the back of c
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    # when either a or b run out just add the rest
    # of the populated list to the end of c
    if not a:
        c += b
    else:
        c += a
    return c

def merge_sort(data):
    """ Sort @data using the Merge Sort technique """

    if not data or len(data) == 1:
        # return if list size is 0 or 1
        return data
    else:
        # split data list in half
        middle = int(len(data) / 2)
        a = merge_sort(data[:middle])
        b = merge_sort(data[middle:])
        # user merge function to merge the two halves
        # back together while also sorting them
        return merge(a, b)

def time_merge_sort(data):
    time_start = time.time()

    merge_sort(data)

    return time.time() - time_start

# time insertion sort
#   uniformly distributed random data
print('insertion sort u 100 : ' +     str(round(insertion_sort(get_u100()),     3)))
print('insertion sort u 1000 : ' +    str(round(insertion_sort(get_u1000()),    3)))
print('insertion sort u 10000 : ' +   str(round(insertion_sort(get_u10000()),   3)))
print('insertion sort u 100000 : ' +  str(round(insertion_sort(get_u100000()),  3)))
print('insertion sort u 1000000 : ' + str(round(insertion_sort(get_u1000000()), 3)))

#   normally distributed random data
print('insertion sort n 100 : ' +     str(round(insertion_sort(get_n100()),     3)))
print('insertion sort n 1000 : ' +    str(round(insertion_sort(get_n1000()),    3)))
print('insertion sort n 10000 : ' +   str(round(insertion_sort(get_n10000()),   3)))
print('insertion sort n 100000 : ' +  str(round(insertion_sort(get_n100000()),  3)))
print('insertion sort n 1000000 : ' + str(round(insertion_sort(get_n1000000()), 3)))

# time bucket sort
#   uniformly distributed data
print('bucket sort u 100 : ' +     str(round(bucket_sort(get_u100()),     3)))
print('bucket sort u 1000 : ' +    str(round(bucket_sort(get_u1000()),    3)))
print('bucket sort u 10000 : ' +   str(round(bucket_sort(get_u10000()),   3)))
print('bucket sort u 100000 : ' +  str(round(bucket_sort(get_u100000()),  3)))
print('bucket sort u 1000000 : ' + str(round(bucket_sort(get_u1000000()), 3)))

#   normally distributed random data
print('bucket sort n 100 : ' +     str(round(bucket_sort(get_n100()),     3)))
print('bucket sort n 1000 : ' +    str(round(bucket_sort(get_n1000()),    3)))
print('bucket sort n 10000 : ' +   str(round(bucket_sort(get_n10000()),   3)))
print('bucket sort n 100000 : ' +  str(round(bucket_sort(get_n100000()),  3)))
print('bucket sort n 1000000 : ' + str(round(bucket_sort(get_n1000000()), 3)))

# time merge sort
#   uniformly distributed data
print('merge sort u 100 : ' +     str(round(time_merge_sort(get_u100()),     3)))
print('merge sort u 1000 : ' +    str(round(time_merge_sort(get_u1000()),    3)))
print('merge sort u 10000 : ' +   str(round(time_merge_sort(get_u10000()),   3)))
print('merge sort u 100000 : ' +  str(round(time_merge_sort(get_u100000()),  3)))
print('merge sort u 1000000 : ' + str(round(time_merge_sort(get_u1000000()), 3)))

#   normally distributed random data
print('merge sort n 100 : ' +     str(round(time_merge_sort(get_n100()),     3)))
print('merge sort n 1000 : ' +    str(round(time_merge_sort(get_n1000()),    3)))
print('merge sort n 10000 : ' +   str(round(time_merge_sort(get_n10000()),   3)))
print('merge sort n 100000 : ' +  str(round(time_merge_sort(get_n100000()),  3)))
print('merge sort n 1000000 : ' + str(round(time_merge_sort(get_n1000000()), 3)))
