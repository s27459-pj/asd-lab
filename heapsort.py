# ruff: noqa


def left(i: int) -> int:
    return 2 * i + 1


def right(i: int) -> int:
    return 2 * i + 2


def max_heapify(heap: list[int], heap_size: int, i: int) -> None:
    l = left(i)
    r = right(i)

    if l < heap_size and heap[l] > heap[i]:
        largest = l
    else:
        largest = i

    if r < heap_size and heap[r] > heap[largest]:
        largest = r

    if i != largest:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, heap_size, largest)


def build_max_heap(heap: list[int]) -> None:
    heap_size = len(heap)
    for i in range(heap_size // 2, -1, -1):
        max_heapify(heap, heap_size, i)


def heap_sort(heap: list[int]) -> list[int]:
    build_max_heap(heap)
    heap_size = len(heap)
    for i in range(heap_size - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heap_size -= 1
        max_heapify(heap, heap_size, 0)

    return heap


def main() -> None:
    heap = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    print(heap)
    heap_sorted = heap_sort(heap)
    print(heap_sorted)


if __name__ == "__main__":
    main()
