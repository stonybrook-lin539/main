from itertools import chain, combinations


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def substrings_of(s):
    substrings = [s[x:y] for x, y in combinations(range(len(s) + 1), r=2)]
    substrings.append('')
    return substrings


def substrings_len_k_of(s, k):
    substrings = [s[x:x + k] for x in range(len(s) + 1 - k)]
    return list(set(substrings))


def subsequences_len_k_of(s, k):
    return(list(set(''.join(c) for c in combinations(s, r=k))))
