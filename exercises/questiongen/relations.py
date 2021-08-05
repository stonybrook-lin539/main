"""
Question generators for relations.
"""

import random
import string
from itertools import product
import io

import PIL.Image

from relation import Relation
import question


def null_op(relation):
    return relation


def relation_props(size=4, edge_ratio=0.5):
    """
    Generate question asking which properties hold of the given relation.

    We take a randomly generated relation and randomly select zero or more
    properties to adjust. Rather than adding symmetry, antisymmetry, or
    asymmetry directly, we modify the presence and absence of self loops and
    pair loops. This procedure ensures even distribution of answer
    combinations.

    We add transitivity only if the current relation is not antisymmetric,
    since this is likely to undo antisymmetry.
    """
    domain = string.ascii_lowercase[:size]
    max_n_edges = 2 ** size
    n_edges = round(edge_ratio * max_n_edges)
    all_pairs = list(product(domain, repeat=2))
    mapping = random.sample(all_pairs, n_edges)
    myrel = Relation(domain, mapping)

    random.choice([Relation.add_reflexive_pairs,
                   Relation.remove_reflexive_pairs,
                   null_op])(myrel)

    random.choice([Relation.add_symmetric_pairs,
                   Relation.remove_symmetric_pairs,
                   null_op])(myrel)

    if not myrel.is_antisymmetric():
        random.choice([Relation.make_transitive, null_op])(myrel)

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
    img = PIL.Image.open(io.BytesIO(buffer))
    return question.MultipleAnswerQuestion(prompt, choices, answers,
                                           promptfigure=img)


if __name__ == "__main__":
    q = relation_props()

    import tkinter as tk
    import PIL.ImageTk
    root = tk.Tk()
    image = PIL.ImageTk.PhotoImage(q.promptfigure)
    label = tk.Label(root, image=image)
    label.pack()
    root.mainloop()
