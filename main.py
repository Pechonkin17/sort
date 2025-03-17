import random
import time
import psutil
import os
import matplotlib.pyplot as plt

from sort import *


array = [random.randint(1, 1000000) for _ in range(10000)]


def measure_performance(sort_function, array):
    """Функція для вимірювання продуктивності сортування"""
    process = psutil.Process(os.getpid())
    memory_before = process.memory_info().rss / 1024

    start_time = time.time()
    sort_function(array.copy())
    end_time = time.time()

    memory_after = process.memory_info().rss / 1024

    execution_time = end_time - start_time
    memory_usage = memory_after - memory_before

    return execution_time, memory_usage


sorting_algorithms = [
    bubble_sort, selection_sort, insertion_sort, gnome_sort, quick_sort,
    merge_sort, heap_sort, shell_sort, counting_sort, radix_sort, bucket_sort, tim_sort
]

execution_times = []
memory_usages = []
algorithm_names = []

for algorithm in sorting_algorithms:
    time_taken, memory_used = measure_performance(algorithm, array)
    execution_times.append(time_taken)
    memory_usages.append(memory_used)
    algorithm_names.append(algorithm.__name__)  # Отримуємо ім'я функції


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.barh(algorithm_names, execution_times, color='blue')
plt.xlabel("Час виконання (сек)")
plt.title("Порівняння часу виконання алгоритмів сортування")

plt.subplot(1, 2, 2)
plt.barh(algorithm_names, memory_usages, color='red')
plt.xlabel("Використання пам’яті (КБ)")
plt.title("Порівняння використання пам'яті алгоритмів сортування")

plt.tight_layout()
plt.show()