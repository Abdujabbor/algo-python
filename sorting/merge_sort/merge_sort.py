from random import randint
import time

def merge_sort(a):
    if len(a) <= 1:
        return a
    m = int(len(a) / 2)
    left = a[:m]
    right = a[m:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    for t in range(len(left) + len(right)):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i < len(left):
            result.append(left[i])
            i += 1
        elif j < len(right):
            result.append(right[j])
            j += 1
    return result


def is_sorted(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True
a = [randint(0, 10 ** 5) for x in range(10 ** 5)]
start_time = time.time()
sorted_a = merge_sort(a)
print("--- %s seconds ---" % (time.time() - start_time))
print(is_sorted(sorted_a))

