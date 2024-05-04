import random
import sys
import timeit
from typing import Callable


def partition(items: list[int], p: int, r: int) -> int:
    pivot = items[r]
    i = p
    for j in range(p, r):
        if items[j] <= pivot:
            items[i], items[j] = items[j], items[i]
            i += 1
    items[r], items[i] = items[i], items[r]
    return i


def quick_sort(items: list[int], p: int, r: int) -> None:
    if p < r:
        q = partition(items, p, r)
        quick_sort(items, p, q - 1)
        quick_sort(items, q + 1, r)


def main_1() -> None:
    items = [5, 7, 4, 1, 2, 8, 3, 6]
    orig_items = items[:]
    print("unsorted", items)
    quick_sort(items, 0, len(items) - 1)
    print("sorted", items)
    print("good?", items == sorted(orig_items))


def partition_weird(items: list[int], p: int, r: int, swap: int) -> int:
    items[r], items[swap] = items[swap], items[r]

    pivot = items[r]
    i = p
    for j in range(p, r):
        if items[j] <= pivot:
            items[i], items[j] = items[j], items[i]
            i += 1
    items[r], items[i] = items[i], items[r]
    return i


def quick_sort_weird(items: list[int], p: int, r: int) -> None:
    if p < r:
        random_swap = random.randint(p, r)
        q = partition_weird(items, p, r, random_swap)
        quick_sort(items, p, q - 1)
        quick_sort(items, q + 1, r)


def main_2() -> None:
    items = [5, 7, 4, 1, 2, 8, 3, 6]
    orig_items = items[:]
    print("unsorted", items)
    quick_sort_weird(items, 0, len(items) - 1)
    print("sorted", items)
    print("good?", items == sorted(orig_items))


def bench(name: str, fn: Callable[[], None], n: int = 1000) -> None:
    total_time = 0
    for _ in range(n):
        start = timeit.default_timer()
        fn()
        end = timeit.default_timer()
        total_time += end - start
    avg_time = total_time / n
    avg_ms = round(avg_time * 1000, 4)
    print(f"{name}: {avg_ms}ms")


def main_3() -> None:
    sys.setrecursionlimit(1500)

    items = [random.randint(0, 100) for _ in range(200)]
    items_sorted = sorted(items)
    items_1, items_2 = items[:], items[:]
    items_sorted_1, items_sorted_2 = items_sorted[:], items_sorted[:]
    r = len(items) - 1

    print(f"bench for {len(items)} items (unsorted list)")
    bench("quick_sort", lambda: quick_sort(items_1, 0, r))
    bench("quick_sort_weird", lambda: quick_sort_weird(items_2, 0, r))

    print()
    print(f"bench for {len(items)} items (sorted list)")
    bench("quick_sort", lambda: quick_sort(items_sorted_1, 0, r))
    bench("quick_sort_weird", lambda: quick_sort_weird(items_sorted_2, 0, r))

    # bench for 200 items (unsorted list)
    # quick_sort: 1.4079ms
    # quick_sort_weird: 0.9035ms
    #
    # bench for 200 items (sorted list)
    # quick_sort: 1.3426ms
    # quick_sort_weird: 0.8828ms
    #
    # quick_sort_weird seems to be faster than quick_sort
    # both sort functions are faster for already sorted lists


main_3()
