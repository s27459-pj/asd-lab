# ruff: noqa

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Self

type Counts = dict[str, int]
type Codes = dict[str, str]


@dataclass
class Node:
    left: Node | None
    right: Node | None
    freq: int
    char: str | None

    def __lt__(self, other: Self) -> bool:
        return self.freq < other.freq

    def __gt__(self, other: Self) -> bool:
        return self.freq > other.freq


def left(i: int) -> int:
    return 2 * i + 1


def right(i: int) -> int:
    return 2 * i + 2


def min_heapify(heap: list[Node], heap_size: int, i: int) -> None:
    l = left(i)
    r = right(i)

    if l < heap_size and heap[l] < heap[i]:
        smallest = l
    else:
        smallest = i

    if r < heap_size and heap[r] < heap[smallest]:
        smallest = r

    if i != smallest:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        min_heapify(heap, heap_size, smallest)


def count_letters(text: str) -> Counts:
    counts: Counts = defaultdict(int)
    for i in text:
        counts[i] += 1
    return counts


def huffmann(nodes: list[Node]) -> Node:
    queue = nodes[:]
    for _ in range(1, len(nodes)):
        min_heapify(queue, len(queue), 0)
        left = queue.pop(0)
        min_heapify(queue, len(queue), 0)
        right = queue.pop(0)
        node = Node(left, right, left.freq + right.freq, None)
        queue.append(node)
    return queue.pop()


def get_huffman_codes(node: Node, code: str = "") -> Codes:
    if node.left is None and node.right is None:
        return {node.char: code}
    return {
        **get_huffman_codes(node.left, code + "0"),
        **get_huffman_codes(node.right, code + "1"),
    }


def encode(cleartext: str, codes: Codes) -> str:
    return "".join(codes[char] for char in cleartext)


def decode(ciphertext: str, root: Node) -> str:
    decoded = ""
    current = root

    for char in ciphertext:
        if char == "0":
            current = current.left
        elif char == "1":
            current = current.right
        if current.left is None and current.right is None:
            decoded += current.char
            current = root

    return decoded


def main() -> None:
    text = "barbara i rabarbar"

    counts = count_letters(text)
    print(counts)

    nodes = huffmann([Node(None, None, freq, char) for char, freq in counts.items()])
    print(nodes)
    codes = get_huffman_codes(nodes)
    print(codes)

    encoded = encode(text, codes)
    print("encoded", encoded)
    decoded = decode(encoded, nodes)
    print("decoded", decoded)


main()
