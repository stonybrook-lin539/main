import random
# from pprint import pprint

import question


SETOPS = {"union": set.union,
          "intersect": set.intersection,
          "difference": set.difference}
SETSYMS = {"union": "∪",
           "intersect": "∩",
           "difference": "\\"}

SET_FOOD = ("apple", "bread", "cheese", "donut", "eggs",
            "fish", "granola", "honey")


def _set_to_str(inset):
    return f"{{{', '.join(inset)}}}"


def set_op_result(domain=SET_FOOD):
    """
    Generate question about result of a set operation.
    """
    opname = random.choice(["union", "intersect", "difference"])
    op = SETOPS[opname]
    opsym = SETSYMS[opname]

    set_a = set(random.sample(domain, k=random.randint(0, 4)))
    set_b = set(random.sample(domain, k=random.randint(0, 4)))
    set_result = op(set_a, set_b)

    prompt = ("Let A, and B be sets such that:"
              f"\n  A = {_set_to_str(set_a)}"
              f"\n  B = {_set_to_str(set_b)}"
              f"\nWhat is the result of A {opsym} B?")
    answer = list(set_result)
    return question.FreeInputQuestion(prompt, answer, "stringlist")


def set_2op_result(domain=SET_FOOD):
    """
    Generate question about result of two union and/or intersection operations.
    """
    opnames = random.choices(["union", "intersect"], k=2)
    op1, op2 = (SETOPS[op] for op in opnames)
    opsym1, opsym2 = (SETSYMS[op] for op in opnames)

    set_a = set(random.sample(domain, k=random.randint(0, 4)))
    set_b = set(random.sample(domain, k=random.randint(0, 4)))
    set_c = set(random.sample(domain, k=random.randint(0, 4)))
    set_result = op2(op1(set_a, set_b), set_c)

    prompt = ("Let A, B, and C be sets such that:"
              f"\n  A = {_set_to_str(set_a)}"
              f"\n  B = {_set_to_str(set_b)}"
              f"\n  C = {_set_to_str(set_c)}"
              f"\nWhat is the result of A {opsym1} B {opsym2} C?")
    answer = list(set_result)
    return question.FreeInputQuestion(prompt, answer, "stringlist")


def which_set_op(domain=SET_FOOD):
    """
    Generate question asking student to fill in the correct set operation.

    Because it's possible for more than one operation to have the same result,
    this function returns a multiple answer question.
    """
    opname = random.choice(["union", "intersect", "difference"])
    op = SETOPS[opname]

    set_a = set(random.sample(domain, k=random.randint(0, 4)))
    set_b = set(random.sample(domain, k=random.randint(0, 4)))
    set_c = op(set_a, set_b)

    is_union = set_c == set_a.union(set_b)
    is_intersection = set_c == set_a.intersection(set_b)
    is_difference = set_c == set_a.difference(set_b)

    answers = []
    if is_union:
        answers.append("union")
    if is_intersection:
        answers.append("intersection")
    if is_difference:
        answers.append("difference")

    prompt = (f"Let A, B, and C be sets such that C is the result of"
              " some operation between A and B. In other words,"
              " C = A _ B."
              f"\n  A = {_set_to_str(set_a)}"
              f"\n  B = {_set_to_str(set_b)}"
              f"\n  C = {_set_to_str(set_c)}"
              f"\nWhat is the operation? There may be more than one answer.")
    return question.FreeInputQuestion(prompt, answers, "stringlist")


def which_set_relation(domain=SET_FOOD):
    """
    Generate question asking student to fill in the correct set relationship.
    """
    domain = random.sample(domain, k=4)

    set_a = set(random.sample(domain, k=random.randint(0, 3)))
    set_b = set(random.sample(domain, k=random.randint(0, 3)))

    answer = None
    if set_a < set_b:
        answer = "proper subset"
    elif set_a > set_b:
        answer = "proper superset"
    elif set_a == set_b:
        answer = "identical"
    elif set_a.isdisjoint(set_b):
        answer = "disjoint"
    else:
        answer = "incomparable"

    prompt = (f"What is the relationship between sets A and B?"
              f"\n  A = {_set_to_str(set_a)}"
              f"\n  B = {_set_to_str(set_b)}"
              f"\nChoose from among the following relationships:"
              "\n  proper subset, proper superset, identical, disjoint,"
              " incomparable")
    return question.FreeInputQuestion(prompt, answer, "string")


if __name__ == "__main__":
    # print(set_op_result())
    # print(set_2op_result())
    print(which_set_op())
    print(which_set_relation())

    # import collections
    # testresults = [q.answer
    #                for q in (which_set_relation()
    #                          for i in range(100))]
    # print(collections.Counter(testresults))
