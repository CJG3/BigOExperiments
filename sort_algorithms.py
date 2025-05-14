import random
import time
import math
import matplotlib.pyplot as plt
import numpy as np


def generate_number_list(listsize):
    return random.sample(range(1, 5 * listsize), listsize)


def quick_sort(the_list, low, high):

    if low < high:
        p = partition(the_list, low, high)

        quick_sort(the_list, low, p - 1)
        quick_sort(the_list, p + 1, high)

    return the_list


def partition(mylist, low, high):
    pivot = mylist[low]
    high = high
    print('pivot: ' + str(pivot))
    print("low:" + str(low))
    print("high:" + str(high))
    print(mylist)
    while low < high:
        while mylist[low] < pivot:
            print(str(mylist[low]) + " is less than  " + str(pivot))
            low += 1

        while mylist[high] > pivot:
            print(str(mylist[high]) + " is greater than " + str(pivot))
            high -= 1
        if low < high:
            mylist[low], mylist[high] = mylist[high], mylist[low]
            print(mylist)

    return high


def test_quicksort(listsize):
    my_list = generate_number_list(listsize)
    print(my_list)
    # quick_sort(my_list, 0, len(my_list) - 1)
    print(quick_sort(my_list, 0, len(my_list) - 1))


def test_merge_sort(listsize):
    my_list = generate_number_list(listsize)
    print(my_list)
    res = merge_sort(my_list)
    print(res)
    return res


def merge_sort(mylist):

    if len(mylist) > 1:
        mid = len(mylist) // 2

        left_side = mylist[:mid]
        right_side = mylist[mid:]

        merge_sort(left_side)
        merge_sort(right_side)

        i = j = k = 0
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                mylist[k] = left_side[i]
                i += 1
            else:
                mylist[k] = right_side[j]
                j += 1
            k += 1

        while i < len(left_side):
            mylist[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            mylist[k] = right_side[j]
            j += 1
            k += 1
    return mylist


def create_datapoints(function, datasize):
    x, y = [], []
    for i in range(10, datasize, 5):

        x.append(i)
        start_time = time.time()
        function(i)
        y.append(time.time() - start_time)
    return x, y
        # print("--- %s seconds ---" % (time.time() - start_time))


def graph_results(function, datasize):
    x, y = create_datapoints(function, datasize)

    plt.plot(x, y)
    plt.xlabel('list size')
    plt.ylabel('time')

    plt.title('Big O performance')
    plt.show()


start_time = time.time()
test_merge_sort(50)
print(time.time() - start_time)
#test_quicksort(10)
#graph_results(test_quicksort, 100)




