#!/usr/bin/env python3

import random
import re


def _biased_increment(bias=0, maximum=0):
    """Increment value probabilistically from 0,
    based on percentage bias up to maximum."""
    base = 0
    while True:
        base += 1
        if random.randint(1, 100) > bias or base >= maximum:
            return base


def _basegenerator(
        alphabet="abcdef",
        emptybias=10,
        sizebias=50,
        maxelements=0,
        ):
    """Generate a random list of unique symbols over the alphabet.

    Parameters
    ----------
    alphabet : str
        string of symbols to build lists from
    emptybias : int
        percentage chance of generating the empty list
    sizebias : int
        percentage chance of adding a new element to the list
    maxelements : int
        maximum length of list
    """
    # return empty set?
    if random.randint(1, 100) <= emptybias:
        return []

    # set a safe maxsize
    if (not maxelements) or (maxelements > len(alphabet)):
        maxelements = len(alphabet)

    # incrementally build a list; higher sizebias builds longer list
    size = _biased_increment(bias=sizebias, maximum=maxelements)
    return random.sample(alphabet, size)


def _setgenerator(
        stopbias=80,
        recursionbias=10,
        singletonrecursionbias=10,
        widthbias=10,
        widthmax=3,
        alphabet="abcdef",
        emptybias=10,
        sizebias=50,
        maxelements=5,
        ):
    """Generate a random set S (possibly empty, possibly nested).

    Parameters
    ----------
    stopbias : int
        Percentage chance of stopping set building after each step
    recursionbias : int
        Percentage chance of building a set containing S
    singletonrecursionbias: int
        Percentage chance of building {S}
    widthbias : int
        Percentage chance of building sets containing many sets
    widthmax : int
        Maximum value of sets contained in a single set
    """
    base = _basegenerator(alphabet=alphabet,
                          emptybias=emptybias,
                          sizebias=sizebias,
                          maxelements=maxelements)
    baseset = frozenset(base)

    while True:
        # should we build something more complex from baseset S?
        if random.randint(1, 100) <= stopbias:
            break

        # do we build flat sets or nested sets?
        recursion = random.randint(1, 100)
        # Case 1: build {S}
        if recursion <= recursionbias and\
           random.randint(1, 100) <= singletonrecursionbias:
            baseset = frozenset([baseset])
        # Case 2: build { a, b, ..., S}
        elif recursion <= recursionbias:
            base = _basegenerator(alphabet=alphabet,
                                  emptybias=emptybias,
                                  sizebias=sizebias,
                                  maxelements=maxelements)
            base.append(baseset)
            baseset = frozenset(base)
        # Case 3: build { A, B, ..., S}
        else:
            # how many sets are we combining S with?
            width = _biased_increment(bias=widthbias, maximum=widthmax)
            base = [_setgenerator(
                stopbias=stopbias,
                recursionbias=recursionbias,
                singletonrecursionbias=singletonrecursionbias,
                widthbias=widthbias,
                widthmax=widthmax,
                alphabet=alphabet,
                sizebias=sizebias,
                emptybias=emptybias,
                maxelements=maxelements,
                ) for _ in range(width)]
            base.append(baseset)
            baseset = frozenset([frozenset(base), baseset])

    return baseset


def _latexify_set(theset):
    setstring = str(theset)
    setstring = re.sub(r"frozenset\(\)", r"\\emptyset", setstring)
    setstring = re.sub(r"frozenset\(", "", setstring)
    setstring = re.sub(r"\)", "", setstring)
    setstring = re.sub(r"\{", "\\{", setstring)
    setstring = re.sub(r"\}", "\\}", setstring)
    setstring = re.sub(r"'", "", setstring)
    return setstring


def _generate_formula(
        sets=[],
        subformulabias=50,
        maxsize=5,
        formulastopbias=80,
        operators=("union", "intersection", "difference"),
        ):
    """Generate a random formula of set operations.

    Parameters
    ----------
    sets : List[Set]
        List of sets to use in construction of formula
    subformulabias : int
        Percentage chance of starting a new subformula from scratch
    maxsize : int
        immediately stop formula building if we have at least {maxsize} sets
    formulastopbias : int
        Percentage chance of stopping formula building
    """
    if not sets:
        return []

    size = 0
    formula = []
    while True:
        # base step: A op B
        if not formula:
            set_a, set_b = random.sample(sets, 2)
            pyop = random.choice(operators)
            formula = [pyop, set_a, set_b]
            size += 1
        # combine with a complex set: (A op B) op (C op D)
        elif random.randint(1, 100) <= subformulabias:
            set_a, set_b = random.sample(sets, 2)
            pyopembed = random.choice(operators)
            pyopmain = random.choice(operators)
            formula = [pyopmain, formula, [pyopembed, set_a, set_b]]
            size += 2
        else:
            set_a = random.choice(sets)
            set_b = formula
            pyop = random.choice(operators)
            formula = [pyop, set_a, set_b]
            size += 1
        if random.randint(1, 100) > formulastopbias or size >= maxsize:
            break
    return formula


def _evaluate_formula(term):
    """Compute set corresponding to formula/term."""
    if isinstance(term, list):
        pyop, term_a, term_b = term
        function = eval(f"frozenset.{pyop}")
        return function(
                _evaluate_formula(term_a),
                _evaluate_formula(term_b))
    return term


def _translate_formula(
        term,
        operators=None,
        ):
    """Translate formla/term into LaTeX code."""
    if operators is None:
        operators = {"union": "\\cup",
                     "intersection": "\\cap",
                     "difference": "-",
                     }
    if isinstance(term, list):
        pyop, term_a, term_b = term
        term_a_string = _translate_formula(term_a)
        term_b_string = _translate_formula(term_b)
        return f"({term_a_string} {operators[pyop]} {term_b_string})"
    return _latexify_set(term)


def generate_setexercise(
        maxsets=5,
        #
        alphabet="abcdef",
        emptybias=10,
        sizebias=50,
        maxelements=5,
        #
        stopbias=80,
        recursionbias=10,
        singletonrecursionbias=10,
        widthbias=10,
        widthmax=3,
        #
        subformulabias=50,
        maxsize=5,
        formulastopbias=80,
        ):
    """Generate a random exercise on set operations.

    Parameters
    ----------
    maxsets : int
        maximum number of sets to build formula from

    _basegenerator Parameters
    -------------------------
    alphabet : str
        string of symbols to build lists from
    emptybias : int
        percentage chance of generating the empty list
    sizebias : int
        percentage chance of adding a new element to the list
    maxelements : int
        maximum length of list

    _setgenerator Parameters
    ------------------------
    stopbias : int
        Percentage chance of stopping set building after each step
    recursionbias : int
        Percentage chance of building a set containing S
    singletonrecursionbias: int
        Percentage chance of building {S}
    widthbias : int
        Percentage chance of building sets containing many sets
    widthmax : int
        Maximum value of sets contained in a single set

    _generate_formula Parameters
    ----------------------------
    subformulabias : int
        Percentage chance of starting a new subformula from scratch
    maxsize : int
        immediately stop formula building if we have at least {maxsize} sets
    formulastopbias : int
        Percentage chance of stopping formula building
    """
    sets = [_setgenerator(
        stopbias=stopbias,
        recursionbias=recursionbias,
        singletonrecursionbias=singletonrecursionbias,
        widthbias=widthbias,
        widthmax=widthmax,
        alphabet=alphabet,
        sizebias=sizebias,
        emptybias=emptybias,
        maxelements=maxelements,
        ) for _ in range(random.randint(2, maxsets))]
    formula = _generate_formula(
            sets=sets,
            subformulabias=subformulabias,
            maxsize=maxsize,
            formulastopbias=formulastopbias,
            )
    result = _evaluate_formula(formula)
    answer = _latexify_set(result)
    latex = _translate_formula(formula)
    prompt = "Compute the set described by the formula below."
    text = f"""::: exercise
{prompt}

$$
{latex[1:-1]}
$$

::: solutiontext

$$
{answer}
$$
:::
:::

"""
    return (text, result)


def create_exercisesheet(batchsize=20,
                         emptysetbias=10,
                         filename=None,
                         title="Exercises with set operations",
                         **kwargs):
    """Generate a sheet of exercises on set operations.

    Parameters
    ----------
    batchsize : int
        number of exercises to generate
    emptysetbias : int
        Percentage chance of including an exercise where the answer is emptyset
    filename : str
        Name of file to store the exercises in
    **kwargs
        See generate_setexercise for details
    """
    if not filename:
        filename = f"{batchsize}_setoperationsexercises.md"
    with open(filename, "a") as exfile:
        exfile.write(f"# {title}\n\n")
        batch = 0
        while True:
            text, result = generate_setexercise(**kwargs)
            if result or random.randint(1, 100) < emptysetbias:
                exfile.write(text)
                batch += 1
            if batch == batchsize:
                break
        # exfile.write("\\includecollection{solutions}")


if __name__ == "__main__":
    # easy exercises
    create_exercisesheet(
        batchsize=100,
        emptysetbias=10,
        filename="setoperations_easy.md",
        title="Exercises with set operations (easy)",
        #
        emptybias=5,
        sizebias=30,
        maxelements=5,
        #
        stopbias=98,
        recursionbias=5,
        singletonrecursionbias=50,
        widthbias=2,
        widthmax=2,
        #
        subformulabias=60,
        maxsize=4,
        formulastopbias=70,
        )
