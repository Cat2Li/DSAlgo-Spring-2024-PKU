from __future__ import annotations
from typing import List, Dict


class TrieNode:

    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False


def build_trie(words: List[str]):
    root = TrieNode()
    for word in words:
        current_node = root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
            # if the word is a prefix of another word, then it is not a valid word
            if current_node.is_end_of_word:
                return False
        current_node.is_end_of_word = True
        # if there are children, then the word is a prefix of another word
        if len(current_node.children):
            return False
    return True


def task():
    N = int(input())
    arr = [input() for _ in range(N)]
    success = build_trie(arr)
    print("YES" if success else "NO")


T = int(input())
[task() for _ in range(T)]
