"""
Question generators for logic.
"""

import random
from itertools import product
from functools import partial

import question
from util import partition

# LOGIC_PRECEDENCE = ["not", "and/or", "conditional", "biconditional"]

LOGIC_OPNAMES_BINARY = ["and", "or", "conditional", "biconditional"]

LOGIC_OPS = {"not": lambda a: int(not a),
             "and": lambda a, b: int(a and b),
             "or": lambda a, b: int(a or b),
             "conditional": lambda a, b: int(not a or b),
             "biconditional": lambda a, b: int(a == b)}

LOGIC_SYMS = {"not": '¬',
              "and": '∧',
              "or": '∨',
              "conditional": '→',
              "biconditional": '↔'}


class Formula:

    def __init__(self, text, func):
        """
        text -- string representation of formula
        func -- executable function with all variables of formula as arguments
        """
        self.text = text
        self.func = func

    # @staticmethod
    # def compose(self, opsym, opfunc, f1, f2=None):
    #     if f2 is not None:
    #         text = f"{f1.text} {opsym} {f2.text}"
    #         def func(*args):
    #             return opfunc(f1(*args), f2(*args))
    #     else:
    #         text = f"{opsym}({f1.text})"
    #         def func(*args):
    #             return opfunc(f1(*args))
    #     return Formula(text, func)

    def __str__(self):
        return f"<Formula {self.text}>"

    def is_equivalent(self, other, n_vars):
        return all(self.func(*args) == other.func(*args)
                   for args in product((1,0), repeat=n_vars))


def _compose_formula(op, f1, f2=None):
    if f2 is not None:
        def f(*args):
            return op(f1(*args), f2(*args))
    else:
        def f(*args):
            return op(f1(*args))
    return f


# def _formulas_are_equivalent(f1, f2, n_vars):
#     return all(f1(*args) == f2(*args) for args in product((1,0), repeat=n_vars))


_formulas_1var_base = [Formula("1", lambda a: 1),
                       Formula("0", lambda a: 0),
                       Formula("a", lambda a: int(a)),
                       Formula("¬a", lambda a: int(not a))]
_formulas_1var = _formulas_1var_base[:]
for opname in LOGIC_OPNAMES_BINARY:
    for lhs, rhs in product(_formulas_1var_base, repeat=2):
        # omit forumulas with no variables
        if lhs.text in ("10") and rhs.text in ("10"):
            continue

        opsym = LOGIC_SYMS[opname]
        opfunc = LOGIC_OPS[opname]

        # add "a op b"
        comp_str = f"{lhs.text} {opsym} {rhs.text}"
        comp_func = _compose_formula(opfunc, lhs.func, rhs.func)
        _formulas_1var.append(Formula(comp_str, comp_func))

_formulas_2var_a = [Formula("a", lambda a, b: int(a)),
                    Formula("¬a", lambda a, b: int(not a))]
_formulas_2var_b = [Formula("b", lambda a, b: int(b)),
                    Formula("¬b", lambda a, b: int(not b))]
_formulas_2var = []
for opname in LOGIC_OPNAMES_BINARY:
    for lhs, rhs in product(_formulas_2var_a, _formulas_2var_b):
        opsym = LOGIC_SYMS[opname]
        opfunc = LOGIC_OPS[opname]

        # add "a op b"
        comp_str = f"{lhs.text} {opsym} {rhs.text}"
        comp_func = _compose_formula(opfunc, lhs.func, rhs.func)
        _formulas_2var.append(Formula(comp_str, comp_func))

        # add "not (a op b)"
        neg_func = LOGIC_OPS["not"]
        neg_comp_str = f"¬({comp_str})"
        neg_comp_func = _compose_formula(neg_func, comp_func)
        _formulas_2var.append(Formula(neg_comp_str, neg_comp_func))

# LOGIC_FORMULAS = {**_formulas_1var, **_formulas_2var}


def _boolfunc(op1, op2):
    return lambda p, q, r: op2(op1(p, q), r)


def logic_op_result():
    """
    Generate question asking student to select which values of P and Q for
    which the given operation evaluates to the given boolean value.
    """
    opname = random.choice(LOGIC_OPNAMES_BINARY)
    myop = LOGIC_OPS[opname]
    mysym = LOGIC_SYMS[opname]
    myresult = random.randint(0, 1)

    prompt = (f"Select all values of P and Q such that P {mysym} Q = {myresult}.")
    boolpairs = [(1,1), (1,0), (0,1), (0,0)]
    choices = [f"P={p}  Q={q}" for p, q in boolpairs]
    answers = [idx for idx, (p, q) in enumerate(boolpairs) if myop(p, q) == myresult]
    return question.MultipleAnswerQuestion(prompt, choices, answers)


def logic_2op_result():
    """
    Generate question asking student to select which values of P, Q, and R for
    which the given operation evaluates to the given boolean value.
    """
    opnames = random.choices(LOGIC_OPNAMES_BINARY, k=2)
    op1, op2 = (LOGIC_OPS[op] for op in opnames)
    sym1, sym2 = (LOGIC_SYMS[op] for op in opnames)
    myfunc = _boolfunc(op1, op2)

    prompt = ("Select all values of P and Q such that"
              f" ((P {sym1} Q) {sym2} R) = 1.")
    booltriples = list(product((1,0), repeat=3))
    choices = [f"P={p}  Q={q}  R={r}" for p, q, r in booltriples]
    answers = [idx for idx, (p, q, r) in enumerate(booltriples) if myfunc(p, q, r) == 1]
    return question.MultipleAnswerQuestion(prompt, choices, answers)


def which_logic_op():
    """
    Generate question asking student to fill in the correct logical operation.

    Because it's possible for more than one operation to have the same result,
    this function returns a multiple answer question.
    """
    opname = random.choice(LOGIC_OPNAMES_BINARY)
    myop = LOGIC_OPS[opname]

    prop_a = random.randint(0, 1)
    prop_b = random.randint(0, 1)
    prop_c = myop(prop_a, prop_b)

    answers = []
    for opname, opfunc in LOGIC_OPS.items():
        if opfunc(prop_a, prop_b) == prop_c:
            answers.append(LOGIC_OPNAMES_BINARY.index(opname))

    prompt = (f"The result of some boolean operation on {prop_a} and {prop_b}"
              f" is {prop_c}."
              f"\nIn other words, {prop_a} _ {prop_b} = {prop_c}."
              f"\nWhat is the operation? There may be more than one answer.")
    choices = LOGIC_OPNAMES_BINARY
    return question.MultipleAnswerQuestion(prompt, choices, answers)


def equivalent_formulas(n_choices=6):
    """
    Generate question asking which formulas are equivalent.
    """
    n_vars = random.choice([1, 2])
    formulas = {1: _formulas_1var, 2: _formulas_2var}[n_vars]
    random.shuffle(formulas)
    target = formulas.pop()

    # select a random set of functions equivalent to the given function
    # we may get fewer results, so we fill the remaining choices based
    # on the actual number of equivalent functions
    n_good_choices = random.randrange(n_choices)
    equivalent_to_target = partial(Formula.is_equivalent, target, n_vars=n_vars)
    good_choices, bad_choices = partition(equivalent_to_target, formulas)
    good_choices = good_choices[:n_good_choices]
    n_bad_choices = n_choices - len(good_choices)
    bad_choices = bad_choices[:n_bad_choices]
    choices = good_choices + bad_choices
    random.shuffle(choices)

    prompt = f"Select all the formulas that are equivalent to {target.text}."
    choicetext = list(c.text for c in choices)
    answeridxlist = [i for i, c in enumerate(choices) if equivalent_to_target(c)]
    return question.MultipleAnswerQuestion(prompt, choicetext, answeridxlist)


if __name__ == "__main__":
    print("One variable formulas")
    print(f"{'formula':10}", "a=1", "a=0", sep=' | ')
    for formula in _formulas_1var:
        s = formula.text
        f = formula.func
        print(f"{s:10}", f"{f(1):3}", f"{f(0):3}", sep=' | ')
    print()

    print("Two variable formulas")
    print(f"{'formula':10}", "a=1", "a=1", "a=0", "a=0", sep=' | ')
    print(f"{'':10}", "b=1", "b=0", "b=1", "b=0", sep=' | ')
    for formula in _formulas_2var:
        s = formula.text
        f = formula.func
        print("{:10}".format(s), f"{f(1,1):3}", f"{f(1,0):3}", f"{f(0,1):3}",
              f"{f(0,0):3}", sep=' | ')
    print()

    q = equivalent_formulas()
    print(q)
