"""
Question generators for relations.
"""

import random
import string
from itertools import product

from relation import Relation
import question


def relation_props(size=4, edge_ratio=0.5):
    """
    Generate question asking which properties hold of the given relation.

    We take a randomly generated relation and randomly select zero or more
    properties to adjust.
    - First, we may add symmetry, antisymmetry, or asymmetry.
    - Next, if not antisymmetric, we may add transitivity, since this is
      likely to undo antisymmetry (and asymmetry).
    - Finally, if not symmetric or antisymmetric (or asymmetric), we may
      add reflexivity or irreflexity, since this would interfere with those
      properties, but not transitivity.
    This procedure ensures a good mix of resulting properties.
    """
    domain = string.ascii_lowercase[:size]
    max_n_edges = 2 ** size
    n_edges = round(edge_ratio * max_n_edges)
    all_pairs = list(product(domain, repeat=2))
    mapping = random.sample(all_pairs, n_edges)
    myrel = Relation(domain, mapping)

    func1 = random.choice([Relation.make_symmetric,
                           Relation.make_antisymmetric,
                           Relation.make_asymmetric,
                           None])
    if func1 is not None:
        func1(myrel)

    if not myrel.is_antisymmetric():
        func2 = random.choice([Relation.make_transitive,
                               None])
        if func2 is not None:
            func2(myrel)

    if not myrel.is_symmetric() and not myrel.is_antisymmetric():
        func3 = random.choice([Relation.make_reflexive,
                               Relation.make_irreflexive,
                               None])
        if func3 is not None:
            func3(myrel)

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
    promptfigure = myrel.to_pydot().create_png()
    return question.MultipleAnswerQuestion(prompt, choices, answers,
                                           promptfigure=promptfigure)


if __name__ == "__main__":
    q = relation_props()

    import tkinter as tk
    import PIL.ImageTk
    root = tk.Tk()
    image = PIL.ImageTk.PhotoImage(data=q.promptfigure)
    label = tk.Label(root, image=image)
    label.pack()
    root.mainloop()
