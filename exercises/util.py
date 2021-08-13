from itertools import chain, combinations, filterfalse, islice, product, tee
import random


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def partition(pred, iterable):
    "Use a predicate to partition entries into true and false entries"
    # partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    t1, t2 = tee(iterable)
    return list(filter(pred, t1)), list(filterfalse(pred, t2))


# def window(iterable, n=2):
#     "Returns a sliding window (of width n) over data from the iterable"
#     "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
#     it = iter(iterable)
#     result = tuple(islice(it, n))
#     if len(result) == n:
#         yield result
#     for elem in it:
#         result = result[1:] + (elem,)
#         yield result


def substrings_of(s):
    substrings = [s[x:y] for x, y in combinations(range(len(s) + 1), r=2)]
    substrings.append('')
    return substrings


def substrings_len_k_of(s, k):
    return list(set([s[x:x+k] for x in range(len(s) + 1 - k)]))


def subsequences_len_k_of(s, k):
    return list(set(''.join(c) for c in combinations(s, r=k)))


def language_sigma_k(alphabet, k):
    return list(''.join(p) for p in product(alphabet, repeat=k))


def language_sigma_up_to_k(alphabet, k):
    return list(chain.from_iterable(
        language_sigma_k(alphabet, i) for i in range(k + 1)))


def random_string(alphabet, k):
    return ''.join(random.choice(alphabet) for i in range(k))


def random_language(alphabet, k, n):
    """
    Return at most n randomly generated strings in the language of strings
    over sigma^k. Fewer strings may be returned if n is smaller than than
    the size of sigma^k, or if several identical strings are generated.
    """
    return list(set(random_string(alphabet, random.randrange(k + 1))
                    for j in range(n)))
