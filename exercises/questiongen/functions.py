"""
Question generators for functions.
"""

import random

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
import PIL.Image

import question


FUNCS = {"flat": lambda x: np.ones_like(x),
         "linear-up": lambda x: x,
         "linear-down": lambda x: -x,
         "quadratic-up": lambda x: x ** 2,
         "quadratic-down": lambda x: -x ** 2,
         "cubic-up": lambda x: x ** 3,
         "cubic-down": lambda x: -x ** 3}

ANSWERS = {"flat": "both",
           "linear-up": "increasing",
           "linear-down": "decreasing",
           "quadratic-up": "neither",
           "quadratic-down": "neither",
           "cubic-up": "increasing",
           "cubic-down": "decreasing"}

CHOICES = ["increasing", "decreasing", "both", "neither"]

FMT_CHOICES = {"increasing": "Increasing (=non-decreasing)",
               "decreasing": "Decreasing (=non-increasing)",
               "both": "Both increasing and decreasing",
               "neither": "Neither increasing nor decreasing"}


def monotonicity():
    """
    Generate question about the monotonicity of the given function.
    """
    funcname = random.choice(list(FUNCS.keys()))
    myfunc = FUNCS[funcname]
    myanswer = ANSWERS[funcname]
    answeridx = CHOICES.index(myanswer)

    x = np.linspace(-2, 2, 100)
    y = myfunc(x)
    fig = Figure(figsize=(3, 2), dpi=96)
    ax = fig.add_subplot()
    # ax.set_ylim(-2, 2)
    ax.plot(x, y)
    canvas = FigureCanvasAgg(fig)
    canvas.draw()

    buffer = fig.canvas.tostring_rgb()
    w, h = fig.canvas.get_width_height()
    img = PIL.Image.frombytes(mode="RGB", size=(w, h), data=buffer)

    prompt = "How can the function depicted be characterized?"
    choices = list(FMT_CHOICES.values())
    return question.MultipleChoiceQuestion(prompt, choices, answeridx,
                                           promptfigure=img)


if __name__ == "__main__":
    q = monotonicity()
    print(q)

    import tkinter as tk
    import PIL.ImageTk
    root = tk.Tk()
    image = PIL.ImageTk.PhotoImage(q.promptfigure)
    label = tk.Label(root, image=image)
    label.pack()
    root.mainloop()
