from __future__ import annotations

from dataclasses import dataclass

type Counts = dict[str, int]
type Codes = dict[str, str]

@dataclass
class Node:
    left: Node | None
    right: Node | None
    freq: int
    char: str | None


def count_letters(text: str) -> Counts:
    counts: Counts = {}
    for i in text:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
    return {k: v for k, v in sorted(counts.items(), key=lambda x: x[1], reverse=True)}


def huffmann(nodes: list[Node]) -> Node:
    queue = nodes[:]
    for i in range(1, len(nodes)):
        left = queue.pop()
        right = queue.pop()
        node = Node(left, right, left.freq + right.freq, None)
        queue.append(node)
    return queue.pop()


def get_huffman_code(node: Node, code: str = "") -> Codes:
    if node.left is None and node.right is None:
        return {node.char: code}
    return {**get_huffman_code(node.left, code + "0"), **get_huffman_code(node.right, code + "1")}


def encode(cleartext: str, codes: Codes) -> str:
    return "".join(codes[char] for char in cleartext)

def decode(ciphertext: str, root: Node) -> str:
    current = root
    decoded = ""

    for char in ciphertext:
        if char == '0':
            current = current.left
        elif char == '1':
            current = current.right
        if current.left is None and current.right is None:
            decoded += current.char
            current = root

    return decoded


def main() -> None:
    # text = "sialababamakniewiedzialajak"
    text = "abbcccddddeeeee"

    counts = count_letters(text)
    print(counts)

    nodes = huffmann([Node(None, None, freq, char) for char, freq in counts.items()])
    print(nodes)
    codes = get_huffman_code(nodes)
    print(codes)

    encoded = encode(text, codes)
    print('encoded', encoded)
    decoded = decode(encoded, nodes)
    print('decoded', decoded)
    print('decoded is good?', decoded == text)


main()
