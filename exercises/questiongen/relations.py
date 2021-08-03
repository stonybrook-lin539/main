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
    """
    domain = string.ascii_lowercase[:size]
    max_n_edges = 2 ** size
    n_edges = round(edge_ratio * max_n_edges)
    all_pairs = list(product(domain, repeat=2))
    mapping = random.sample(all_pairs, n_edges)
    myrel = Relation(domain, mapping)

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
