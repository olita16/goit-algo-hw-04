import timeit
import random
import matplotlib.pyplot as plt
from colorama import Fore, Style, init

init(autoreset=True)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def run_sort_tests(sizes, use_colors=True):
    insertion_times = []
    merge_times = []
    timsort_times = []
    
    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        
        if use_colors:
            print(Style.BRIGHT + Fore.CYAN + f"\n🔍 Розмір масиву: {size}")
        else:
            print(f"\nArray size: {size}")

        # Insertion Sort
        if size <= 1000:
            t_ins = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
            insertion_times.append(t_ins)
            msg = f"Insertion Sort: {t_ins:.6f} сек"
            print(Style.BRIGHT + Fore.YELLOW + msg if use_colors else msg)
        else:
            insertion_times.append(None)
            msg = "⚠️ Insertion Sort: Пропущено (занадто великий розмір)"
            print(Style.DIM + Fore.YELLOW + msg if use_colors else msg)

        # Merge Sort
        t_merge = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)
        merge_times.append(t_merge)
        msg_merge = f"Merge Sort:     {t_merge:.6f} сек"
        print(Style.BRIGHT + Fore.GREEN + msg_merge if use_colors else msg_merge)

        # Timsort
        t_tim = timeit.timeit(lambda: sorted(arr.copy()), number=1)
        timsort_times.append(t_tim)
        msg_tim = f"Timsort:        {t_tim:.6f} сек"
        print(Style.BRIGHT + Fore.MAGENTA + msg_tim if use_colors else msg_tim)

    return insertion_times, merge_times, timsort_times

# Test
sizes = [100, 500, 1000, 2000, 5000, 10000]
insertion_times, merge_times, timsort_times = run_sort_tests(sizes, use_colors=True)

# Results in char
plt.figure(figsize=(10, 6))
plt.plot(sizes, insertion_times, label='Insertion Sort', color='yellow', marker='o')
plt.plot(sizes, merge_times, label='Merge Sort', color='green', marker='o')
plt.plot(sizes, timsort_times, label='Timsort', color='magenta', marker='o')

plt.title('Час виконання сортувань в залежності від розміру масиву')
plt.xlabel('Розмір масиву')
plt.ylabel('Час (секунди)')
plt.legend()

# Show char
plt.grid(True)
plt.show()
