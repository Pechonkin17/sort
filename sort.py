#   O(n^2)
def bubble_sort(args):
    n = len(args)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if args[j] > args[j + 1]:
                args[j], args[j + 1] = args[j + 1], args[j]
    return args


#   O(n^2)
def insertion_sort(args):
    n = len(args)
    i = 1
    while i < n:
        key = args[i]
        j = i - 1
        while j >= 0 and key < args[j]:
            args[j + 1] = args[j]
            j -= 1
        i += 1
        args[j + 1] = key
    return args


#   O(n^2)
def selection_sort(args):
    n = len(args)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if args[j] < args[min_idx]:
                min_idx = j
        args[i], args[min_idx] = args[min_idx], args[i]
    return args


#   O(n^2)
def gnome_sort(args):
    i = 0
    while i < len(args):
        if i == 0 or args[i] >= args[i-1]:
            i += 1
        else:
            args[i], args[i-1] = args[i-1], args[i]
    return args


#   O(n^2)
def quick_sort(args):
    n = len(args)
    if n <= 1:
        return args

    pivot = args[-1]

    less = [x for x in args[:-1] if x <= pivot]
    greater = [x for x in args[:-1] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


#   O(n * log(n))
def merge_sort(args):
    n = len(args)
    if n > 1:
        mid = n // 2
        left_half = args[:mid]
        right_half = args[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                args[k] = left_half[i]
                i += 1
            else:
                args[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            args[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            args[k] = right_half[j]
            j += 1
            k += 1
    return args


#   O(n * log(n))
def heap_sort(args):
    def heapify(args, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and args[left] > args[largest]:
            largest = left

        if right < n and args[right] > args[largest]:
            largest = right

        if largest != i:
            args[i], args[largest] = args[largest], args[i]
            heapify(args, n, largest)


    n = len(args)
    for i in range(n // 2 - 1, -1, -1):
        heapify(args, n, i)

    for i in range(n - 1, 0, -1):
        args[i], args[0] = args[0], args[i]
        heapify(args, i, 0)

    return args


#   O(n log² n)
def shell_sort(args):
    n = len(args)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = args[i]
            j = i
            while j >= gap and args[j - gap] > temp:
                args[j] = args[j - gap]
                j -= gap
            args[j] = temp
        gap //= 2
    return args


#    (O(n + k)), де n — кількість елементів у масиві, а k — максимальне значення в масиві.
def counting_sort(args):
    max_val = max(args)
    min_val = min(args)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(args)

    for num in args:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(args):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output


#   (O(nk)), де n — кількість елементів у масиві, а k — кількість цифр у найбільшому числі.
def radix_sort(args):
    def counting_sort_radix(args, exp):
        n = len(args)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = args[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = args[i] // exp
            output[count[index % 10] - 1] = args[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            args[i] = output[i]


    max_val = max(args)
    exp = 1

    while max_val // exp > 0:
        counting_sort_radix(args, exp)
        exp *= 10
    return args


# O(n log n)
def bucket_sort(args):
    if len(args) == 0:
        return args

    max_val = max(args)
    size = max_val / len(args)

    buckets = [[] for _ in range(len(args))]

    for i in range(len(args)):
        index = int(args[i] // size)
        if index != len(args):
            buckets[index].append(args[i])
        else:
            buckets[len(args) - 1].append(args[i])

    for i in range(len(args)):
        buckets[i] = sorted(buckets[i])

    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result


#   O(n log n) / O(n)
def tim_sort(args):
    def insertion_sort(args, left, right):
        for i in range(left + 1, right + 1):
            key = args[i]
            j = i - 1
            while j >= left and args[j] > key:
                args[j + 1] = args[j]
                j -= 1
            args[j + 1] = key

    def merge(args, left, mid, right):
        len1, len2 = mid - left + 1, right - mid
        left_part, right_part = args[left:left + len1], args[mid + 1:mid + 1 + len2]

        i, j, k = 0, 0, left
        while i < len1 and j < len2:
            if left_part[i] <= right_part[j]:
                args[k] = left_part[i]
                i += 1
            else:
                args[k] = right_part[j]
                j += 1
            k += 1

        while i < len1:
            args[k] = left_part[i]
            i += 1
            k += 1

        while j < len2:
            args[k] = right_part[j]
            j += 1
            k += 1
    n = len(args)
    RUN = 32

    for i in range(0, n, RUN):
        insertion_sort(args, i, min(i + RUN - 1, n - 1))

    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(args, left, mid, right)
        size *= 2

    return args