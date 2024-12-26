# https://open.kattis.com/problems/kikiboba

def is_boba(word: str) -> bool:
    return word.count('b') > word.count('k')


def is_none(word: str) -> bool:
    return (word.count('b') + word.count('k')) == 0


def is_boki(word: str) -> bool:
    return word.count('b') == word.count('k') and not is_none(word)


def is_kiki(word: str) -> bool:
    return not is_boba(word) and not is_boki(word) and not is_none(word)


word = input()
if is_boba(word):
    print("boba")
elif is_boki(word):
    print("boki")
elif is_kiki(word):
    print("kiki")
else:
    print("none")
