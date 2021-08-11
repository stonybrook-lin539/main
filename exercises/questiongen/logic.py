"""
Question generators for logic.
"""

import random
from itertools import product

import question

# LOGIC_PRECEDENCE = ["not", "and/or", "conditional", "biconditional"]

LOGIC_OPNAMES = ["and", "or", "conditional", "biconditional"]

LOGIC_OPS = {"and": lambda a, b: int(a and b),
             "or": lambda a, b: int(a or b),
             "conditional": lambda a, b: int(not a or b),
             "biconditional": lambda a, b: int(a == b)}

LOGIC_SYMS = {"and": '∧',
              "or": '∨',
              "conditional": '→',
              "biconditional": '↔'}


def _boolfunc(op1, op2):
    return lambda p, q, r: op2(op1(p, q), r)


def logic_op_result():
    """
    Generate question asking student to select which values of P and Q for
    which the given operation evaluates to the given boolean value.
    """
    opname = random.choice(LOGIC_OPNAMES)
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
    opnames = random.choices(LOGIC_OPNAMES, k=2)
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
    opname = random.choice(LOGIC_OPNAMES)
    myop = LOGIC_OPS[opname]

    prop_a = random.randint(0, 1)
    prop_b = random.randint(0, 1)
    prop_c = myop(prop_a, prop_b)

    answers = []
    for opname, opfunc in LOGIC_OPS.items():
        if opfunc(prop_a, prop_b) == prop_c:
            answers.append(LOGIC_OPNAMES.index(opname))

    prompt = (f"The result of some boolean operation on {prop_a} and {prop_b}"
              f" is {prop_c}."
              f"\nIn other words, {prop_a} _ {prop_b} = {prop_c}."
              f"\nWhat is the operation? There may be more than one answer.")
    choices = LOGIC_OPNAMES
    return question.MultipleAnswerQuestion(prompt, choices, answers)


if __name__ == "__main__":
    q = logic_2op_result()
    print(q)
