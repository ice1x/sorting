import random
from datetime import datetime


def getArray():
    return [int(10000 * random.random()) for i in range(10000)]


def shellSort(data):
    """
    Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1.
    """
    gap = len(data) // 2
    # loop over the gaps
    while gap > 0:
        # do the insertion sort
        for i in range(gap, len(data)):
            val = data[i]
            j = i
            while j >= gap and data[j - gap] > val:
                data[j] = data[j - gap]
                j -= gap
            data[j] = val
        gap //= 2
    return data


def bubble(data):
    """
    Ops: O(n^2)
    """
    n = 1
    while n < len(data):
        for i in range(len(data) - n):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        n += 1
    return data


def quicksort_original(data):
    """
    Ops: O(n log n), worst case: O(n^2)
    """
    if len(data) <= 1:
        return data
    else:
        q = random.choice(data)
        s_data = []
        m_data = []
        e_data = []
        for n in data:
            if n < q:
                s_data.append(n)
            elif n > q:
                m_data.append(n)
            else:
                e_data.append(n)
        return quicksort_original(s_data) + e_data + quicksort_original(m_data)


def quicksort_optimized(data, fst, lst):
    """
    memory utilization optimized
    """
    if fst >= lst: return

    i, j = fst, lst
    pivot = data[random.randint(fst, lst)]

    while i <= j:
        while data[i] < pivot: i += 1
        while data[j] > pivot: j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
            i, j = i + 1, j - 1
    quicksort_optimized(data, fst, j)
    quicksort_optimized(data, i, lst)
    return data


nums = getArray()
t_start = datetime.now()
out = shellSort(nums)
t_end = datetime.now() - t_start
print('shellSort', t_end)

nums = getArray()
t_start = datetime.now()
out = bubble(nums)
t_end = datetime.now() - t_start
print('bubble', t_end)

nums = getArray()
t_start = datetime.now()
out = quicksort_original(nums)
t_end = datetime.now() - t_start
print('quicksort_original', t_end)

nums = getArray()
t_start = datetime.now()
out = quicksort_optimized(nums, 0, len(nums) - 1)
t_end = datetime.now() - t_start
print('quicksort_optimized', t_end)
