"""
Question generators for FSAs.
"""

import random

import question
from fsagen import *
from util import pil_open_from_memory


def fsa_to_language(n_choices=4):
    """
    Generate question about language of a given FSA.
    """
    fsa_set = random.choice(FSA_SETS)
    fsas = random.sample(fsa_set, n_choices)

    answeridx = random.randrange(n_choices)
    target_fsa = fsas[answeridx][0]

    prompt = "What language is generated by the FSA shown below?"
    buffer = target_fsa.to_pydot().create_png()
    img = pil_open_from_memory(buffer)
    choices = [desc for fsa, desc in fsas]
    return question.MultipleChoiceQuestion(prompt, choices, answeridx,
                                           promptfigure=img)


def language_to_fsa(n_choices=4):
    """
    Generate question about FSA for a given language.
    """
    fsa_set = random.choice(FSA_SETS)
    fsas = random.sample(fsa_set, n_choices)

    answeridx = random.randrange(n_choices)
    target_fsa_desc = fsas[answeridx][1]

    prompt = ("Choose the FSA corresponding to the following language:"
              f"\n  {target_fsa_desc}")
    buffers = [fsa.to_pydot().create_png() for fsa, desc in fsas]
    choices = [pil_open_from_memory(b) for b in buffers]
    return question.MultipleChoiceQuestion(prompt, choices, answeridx,
                                           answertype="image")


FSAS_2SYM = [
    even_a(2, 0),
    even_a(2, 1),
    odd_a(2, 0),
    odd_a(2, 1),
    exactly_2_a(2,0),
    exactly_2_a(2,1),
    set_abc_star(2),
    set_abc_plus(2),
    seq_abc_star(2),
    seq_abc_plus(2),
    a_star_b_star(),
    a_plus_b_plus()
]

FSAS_3SYM = [
    even_a(3, 0),
    even_a(3, 1),
    even_a(3, 2),
    exactly_2_a(3,0),
    exactly_2_a(3,1),
    exactly_2_a(3,2),
    set_abc_star(3),
    set_abc_plus(3),
    seq_abc_star(3),
    seq_abc_plus(3),
]

FSA_SETS = [FSAS_2SYM, FSAS_3SYM]


def test():
    q1 = fsa_to_language()
    print(q1)

    q2 = language_to_fsa()
    print(q2)

    # from util import tk_show_image
    # tk_show_image(q1.promptfigure)
    # tk_show_image(*q2.choices)


if __name__ == "__main__":
    test()
