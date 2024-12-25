# https://open.kattis.com/problems/kikiboba

import sys
import unittest


def is_boba(word: str) -> bool:
    return word.count('b') > word.count('k')


def is_none(word: str) -> bool:
    return (word.count('b') + word.count('k')) == 0


def is_boki(word: str) -> bool:
    return word.count('b') == word.count('k') and not is_none(word)


def is_kiki(word: str) -> bool:
    return not is_boba(word) and not is_boki(word) and not is_none(word)


def categorize(word: str) -> str:
    if is_boba(word):
        return "boba"
    if is_boki(word):
        return "boki"
    if is_kiki(word):
        return "kiki"
    return "none"


def run():
    for word in sys.stdin:
        category = categorize(word)
        print(category)
        break


if __name__ == "__main__":
    run()
