"""
Question generators for functions.
"""

import random

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
import PIL.Image

import question

FUNCS = {
    "flat": lambda x: np.ones_like(x),
    "linear-up": lambda x: x,
    "linear-down": lambda x: -x,
    "quadratic-up": lambda x: x**2,
    "quadratic-down": lambda x: -x**2,
    "cubic-flat-up": lambda x: x**3,
    "cubic-flat-down": lambda x: -x**3,
    "cubic-curvy-up": lambda x: x**3 - 2 * x,
    "cubic-curvy-down": lambda x: - x**3 + 2 * x,
    "logistic-up": lambda x: 1 / (1 + np.e ** (-2*x)),
    "logistic-down": lambda x: 1 / (1 + np.e ** (-2*x)),
    "piecewise-up":
        lambda x: np.piecewise(x, [x < -1, x >= -1, x >= 1],
                               [lambda x: 1 + x,
                                lambda x: 0,
                                lambda x: -1 + x]),
    "piecewise-down":
        lambda x: np.piecewise(x, [x < -1, x >= -1, x >= 1],
                               [lambda x: -1 - x,
                                lambda x: 0,
                                lambda x: 1 - x])
}

FUNCS_INC_STR = ["linear-up", "cubic-flat-up", "logistic-up"]
FUNCS_DEC_STR = ["linear-down", "cubic-flat-down", "logistic-down"]
FUNCS_INC_NONSTR = ["flat", "piecewise-up"]
FUNCS_DEC_NONSTR = ["flat", "piecewise-down"]
FUNCS_INC_ALL = FUNCS_INC_STR + FUNCS_INC_NONSTR
FUNCS_DEC_ALL = FUNCS_DEC_STR + FUNCS_DEC_NONSTR
# FUNCS_BOTH = ["flat"]
# FUNCS_NEITHER = ["quadratic-up", "quadratic-down", "cubic-curvy-up",
#                  "cubic-curvy-down"]

CHOICES_IDBN = ["increasing", "decreasing", "both", "neither"]

FMT_CHOICES_IDBN = {
    "increasing": "Increasing",
    "decreasing": "Decreasing",
    "both": "Both increasing and decreasing",
    "neither": "Neither increasing nor decreasing"}

ANSWERS_IDBN = {
    "flat": "both",
    "linear-up": "increasing",
    "linear-down": "decreasing",
    "quadratic-up": "neither",
    "quadratic-down": "neither",
    "cubic-flat-up": "increasing",
    "cubic-flat-down": "decreasing",
    "cubic-curvy-up": "neither",
    "cubic-curvy-down": "neither",
    "logistic-up": "increasing",
    "logistic-down": "decreasing",
    "piecewise-up": "increasing",
    "piecewise-down": "decreasing"}

CHOICES_STR_NSTR = ["increasing", "decreasing", "inc-strict", "dec-strict",
                    "inc-nonstrict", "dec-nonstrict"]

FMT_CHOICES_STR_NSTR = {
    "increasing": "increasing",
    "decreasing": "decreasing",
    "inc-strict": "strictly increasing",
    "dec-strict": "strictly decreasing",
    "inc-nonstrict": "increasing but not strictly increasing",
    "dec-nonstrict": "decreasing but not strictly decreasing"}

ANSWERS_STR_NSTR = {
    "increasing": FUNCS_INC_ALL,
    "decreasing": FUNCS_DEC_ALL,
    "inc-strict": FUNCS_INC_STR,
    "dec-strict": FUNCS_DEC_STR,
    "inc-nonstrict": FUNCS_INC_NONSTR,
    "dec-nonstrict": FUNCS_DEC_NONSTR}


def func_to_monotonicity():
    """
    Generate question asking student to choose whether the given function is
    increasing, decreasing, both, or neither.
    """
    funcname = random.choice(list(FUNCS.keys()))
    myfunc = FUNCS[funcname]
    myanswer = ANSWERS_IDBN[funcname]
    answeridx = CHOICES_IDBN.index(myanswer)

    prompt = "Is the function shown below increasing or decreasing?"
    img = _func_to_image(myfunc)
    choices = list(FMT_CHOICES_IDBN.values())
    return question.MultipleChoiceQuestion(prompt, choices, answeridx,
                                           promptfigure=img)


def monotonicity_to_function():
    """
    Generate question asking student to select the (strictly or nonstrictly)
    increasing or decreasing functions.
    """
    functype = random.choice(CHOICES_STR_NSTR)
    funcnames = random.sample(list(FUNCS.keys()), 4)
    answeridxlist = [funcnames.index(fname) for fname in funcnames
                     if fname in ANSWERS_STR_NSTR[functype]]

    fmt_functype = FMT_CHOICES_STR_NSTR[functype]
    prompt = f"Select all the functions that are {fmt_functype}."
    choices = [_func_to_image(FUNCS[fname], figsize=(2, 1))
               for fname in funcnames]
    return question.MultipleAnswerQuestion(prompt, choices, answeridxlist,
                                           answertype="image")


def _func_to_image(func, figsize=(3, 2)):
    x = np.linspace(-2, 2, 100)
    y = func(x)
    fig = Figure(figsize=figsize, dpi=96)
    ax = fig.add_subplot()
    # ax.set_ylim(-2, 2)
    ax.plot(x, y)
    canvas = FigureCanvasAgg(fig)
    canvas.draw()

    buffer = fig.canvas.tostring_rgb()
    w, h = fig.canvas.get_width_height()
    img = PIL.Image.frombytes(mode="RGB", size=(w, h), data=buffer)
    return img


if __name__ == "__main__":
    q = monotonicity_to_function()
    print(q)

    # import tkinter as tk
    # import PIL.ImageTk
    # root = tk.Tk()
    # image = PIL.ImageTk.PhotoImage(q.promptfigure)
    # label = tk.Label(root, image=image)
    # label.pack()
    # root.mainloop()
