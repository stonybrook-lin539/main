"""
Question generators for relations.
"""

import random
import string
from itertools import product

from relation import Relation
import question
from util import pil_open_from_memory


def _null_op(relation):
    return relation


def relation_props(size=4, edge_ratio=0.5):
    """
    Generate question asking which properties hold of the given relation.

    Parameters:
      size -- number of elements
      edge_ratio -- proportion of possible edges to include before modifications

    We take a randomly generated relation and randomly select zero or more
    properties to adjust. Rather than adding symmetry, antisymmetry, or
    asymmetry directly, we modify the presence and absence of self loops and
    pair loops. We add transitivity only if the current relation is not
    antisymmetric, since this is likely to undo antisymmetry. This procedure
    ensures even distribution of answer combinations.
    """
    domain = string.ascii_lowercase[:size]
    max_n_edges = 2 ** size
    n_edges = round(edge_ratio * max_n_edges)
    all_pairs = list(product(domain, repeat=2))
    mapping = random.sample(all_pairs, n_edges)
    myrel = Relation(domain, mapping)

    random.choice([Relation.add_reflexive_pairs,
                   Relation.remove_reflexive_pairs,
                   _null_op])(myrel)

    random.choice([Relation.add_symmetric_pairs,
                   Relation.remove_symmetric_pairs,
                   _null_op])(myrel)

    if not myrel.is_antisymmetric():
        random.choice([Relation.make_transitive, _null_op])(myrel)

    choices = ["reflexive", "irreflexive", "transitive", "symmetric",
               "antisymmetric", "asymmetric"]
    answers = []
    if myrel.is_reflexive():
        answers.append(choices.index("reflexive"))
    if myrel.is_irreflexive():
        answers.append(choices.index("irreflexive"))
    if myrel.is_transitive():
        answers.append(choices.index("transitive"))
    if myrel.is_symmetric():
        answers.append(choices.index("symmetric"))
    if myrel.is_antisymmetric():
        answers.append(choices.index("antisymmetric"))
    if myrel.is_asymmetric():
        answers.append(choices.index("asymmetric"))

    prompt = "What properties hold of the relation depicted in the image below?"
    buffer = myrel.to_pydot().create_png()
    img = pil_open_from_memory(buffer)
    return question.MultipleAnswerQuestion(prompt, choices, answers,
                                           promptfigure=img)


def test():
    q = relation_props()
    print(q)
    # from util import tk_show_image
    # tk_show_image(q.promptfigure)


if __name__ == "__main__":
    test()
