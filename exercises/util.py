"""
Utility functions for iteration, strings/languages, images.
"""

from itertools import chain, combinations, filterfalse, product, tee
import random

import io
import PIL.Image


def powerset(iterable):
    """
    Return generator containing powerset of elements in given iterable.

    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def partition(pred, iterable):
    """
    Use a predicate to partition entries into true and false entries, returned
    as tuple of two lists.

    partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    """
    t1, t2 = tee(iterable)
    return list(filter(pred, t1)), list(filterfalse(pred, t2))


def padlr(string, left, right, n):
    """Pad `string` with `n` copies each of `left` and `right`."""
    return f"{left * n}{string}{right * n}"


def substrings_of(s):
    """Return list of all substrings of given string."""
    substrings = [s[x:y] for x, y in combinations(range(len(s) + 1), r=2)]
    substrings.append('')
    return substrings


def substrings_len_k_of(s, k):
    """Return list of all length `k` substrings of string `s`."""
    return list(set([s[x:x+k] for x in range(len(s) + 1 - k)]))


def subsequences_len_k_of(s, k):
    """Return list of all length `k` subsequences of string `s`."""
    return list(set(''.join(c) for c in combinations(s, r=k)))


def language_sigma_k(alphabet, k):
    """
    Return list of all strings over `alphabet` of length `k`.
    """
    return list(''.join(p) for p in product(alphabet, repeat=k))


def language_sigma_up_to_k(alphabet, k):
    """
    Return list of all strings over `alphabet` of length **up to** `k`.
    """
    return list(chain.from_iterable(
        language_sigma_k(alphabet, i) for i in range(k + 1)))


def random_string(alphabet, k):
    """
    Return a string consisting of `k` symbols randomly selected from
    `alphabet`.
    """
    return ''.join(random.choice(alphabet) for i in range(k))


def random_language(alphabet, k, n):
    """
    Return at most n randomly generated strings in the language of strings
    over sigma^k. Fewer strings may be returned if n is smaller than than
    the size of sigma^k, or if several identical strings are generated.
    """
    return list(set(random_string(alphabet, random.randrange(k + 1))
                    for j in range(n)))


def pil_open_from_memory(filebytes):
    """
    Open an image file (PNG, etc.) already in memory. This is different
    from creating an image from raw bytes.
    """
    return PIL.Image.open(io.BytesIO(filebytes))


def tk_show_image(*imgs):
    """
    Show one or more PIL images using Tkinter. For testing purposes.
    """
    import tkinter as tk
    import PIL.ImageTk
    root = tk.Tk()
    tkimages = [PIL.ImageTk.PhotoImage(img) for img in imgs]
    for tkimage in tkimages:
        imglabel = tk.Label(root, image=tkimage)
        imglabel.pack()
    root.mainloop()
