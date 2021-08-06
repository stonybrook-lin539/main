import string

from fsa import FSA


def even_a(alphsize=3, i=0):
    """Even number of some symbol. Number of other symbols is irrelevant."""
    alph = string.ascii_lowercase[:alphsize]
    a = alph[i]
    q0 = 0
    qs = {0, 1}
    fs = {0}

    ts = {}
    for x in alph:
        ts[0, x] = 0
        ts[1, x] = 1

    ts[0, a] = 1
    ts[1, a] = 0

    fsa = FSA(qs, alph, q0, fs, ts)
    desc = f"Even number of {a}'s"
    return fsa, desc


def odd_a(alphsize=3, i=0):
    """Even number of some symbol. Number of other symbols is irrelevant."""
    alph = string.ascii_lowercase[:alphsize]
    a = alph[i]
    q0 = 0
    qs = {0, 1}
    fs = {1}

    ts = {}
    for x in alph:
        ts[0, x] = 0
        ts[1, x] = 1

    ts[0, a] = 1
    ts[1, a] = 0

    fsa = FSA(qs, alph, q0, fs, ts)
    desc = f"Odd number of {a}'s"
    return fsa, desc


def exactly_2_a(alphsize=3, i=0):
    """Exactly two of some symbol. Number of other symbols is irrelevant."""
    alph = string.ascii_lowercase[:alphsize]
    a = alph[i]
    q0 = 0
    qs = {0, 1, 2, 3}
    fs = {2}

    ts = {}
    for x in alph:
        ts[0, x] = 0
        ts[1, x] = 1
        ts[2, x] = 2
        ts[3, x] = 3

    ts[0, a] = 1
    ts[1, a] = 2
    ts[2, a] = 3
    ts[3, a] = 3

    fsa = FSA(qs, alph, q0, fs, ts)
    desc = f"Exactly two {a}'s"
    return fsa, desc


def set_abc_star(alphsize=2, **kwargs):
    """Any number of any symbol."""
    alph = string.ascii_lowercase[:alphsize]
    q0 = 0
    qs = {0}
    fs = {0}

    ts = {}
    for x in alph:
        ts[0, x] = 0

    fsa = FSA(qs, alph, q0, fs, ts)
    desc = f"{{{','.join(alph)}}}*"
    return fsa, desc


def set_abc_plus(alphsize=2, **kwargs):
    """At least one of any symbol."""
    alph = string.ascii_lowercase[:alphsize]
    q0 = 0
    qs = {0, 1}
    fs = {0, 1}

    ts = {}
    for x in alph:
        ts[0, x] = 1
        ts[1, x] = 1

    fsa = FSA(qs, alph, q0, fs, ts)
    desc = f"{{{','.join(alph)}}}+"
    return fsa, desc


def seq_abc_star(alphsize=2, **kwargs):
    """Any number of repetitions of sequence."""
    alph = string.ascii_lowercase[:alphsize]
    q0 = 0
    qs = {i for i in range(alphsize)}
    fs = {0}

    ts = {}
    for i, x in enumerate(alph):
        ts[i, x] = (i + 1) % alphsize

    fsa = FSA(qs, alph, q0, fs, ts)
    desc = f"({alph})*"
    return fsa, desc


def seq_abc_plus(alphsize=2, **kwargs):
    """One or more repetitions of sequence."""
    alph = string.ascii_lowercase[:alphsize]
    q0 = 0
    qs = {i for i in range(alphsize + 1)}
    fs = {alphsize + 1}

    ts = {}
    for i, x in enumerate(alph):
        ts[i, x] = (i + 1)
    ts[alphsize, alph[0]] = 1

    fsa = FSA(qs, alph, q0, fs, ts)
    desc = f"({alph})+"
    return fsa, desc


def a_star_b_star(**kwargs):
    """Any number of a's followed by any number of b's."""
    alph = "ab"
    q0 = 0
    qs = {0,  # start
          1,  # seen an 'a'
          2,  # seen a 'b''
          3}  # saw a 'b'' before an 'a', or an 'a' after a 'b'
    fs = {0, 1, 2}
    ts = {(0, 'a'): 1,
          (0, 'b'): 2,
          (1, 'a'): 1,
          (1, 'b'): 2,
          (2, 'a'): 3,
          (2, 'b'): 2,
          (3, 'a'): 3,
          (3, 'b'): 3}

    fsa = FSA(qs, alph, q0, fs, ts)
    desc = f"a*b*"
    return fsa, desc


def a_plus_b_plus(**kwargs):
    """One or more of a's followed by one or more b's."""
    alph = "ab"
    q0 = 0
    qs = {0,  # start
          1,  # seen an 'a'
          2,  # seen a 'b''
          3}  # saw a 'b'' before an 'a', or an 'a' after a 'b'
    fs = {2}
    ts = {(0, 'a'): 1,
          (0, 'b'): 3,
          (1, 'a'): 1,
          (1, 'b'): 2,
          (2, 'a'): 3,
          (2, 'b'): 2,
          (3, 'a'): 3,
          (3, 'b'): 3}

    fsa = FSA(qs, alph, q0, fs, ts)
    desc = f"a+b+"
    return fsa, desc
