#!/usr/bin/python3
"""Determines if all boxes can be opened using DFS."""


def canUnlockAll(boxes):
    """Check if all boxes can be unlocked."""
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    visited = set([0])
    stack = [0]

    while stack:
        current = stack.pop()
        for key in boxes[current]:
            if isinstance(key, int) and 0 <= key < n and key not in visited:
                visited.add(key)
                stack.append(key)

    return len(visited) == n
