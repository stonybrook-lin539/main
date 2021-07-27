import tkinter as tk
from tkinter import ttk


import questiongen as qgen


class Gui(ttk.Frame):

    def __init__(self):
        super().__init__()
        self.qgen = qgen.which_set_relation
        self.currquestion = self.qgen()
        self._init_ui()

    def _init_ui(self):
        self.inputvar = tk.StringVar()

        self.heading = ttk.Label(self, text="Set Question")
        self.prompt = ttk.Label(self, text=self.currquestion.prompt, wraplength=400)
        self.entry = ttk.Entry(self, textvariable=self.inputvar)
        self.response = ttk.Label(self,
                                  text="Enter your answer.")

        self.buttongrid = ttk.Frame(self)
        self.check_btn = ttk.Button(self.buttongrid,
                                    text="Check Answer",
                                    command=self._check_answer)
        self.show_btn = ttk.Button(self.buttongrid,
                                   text="Show Answer",
                                   command=self._show_answer)
        self.next_btn = ttk.Button(self.buttongrid,
                                   text="Next Question",
                                   command=self._next_question)

        self.pack(fill="both", expand=True)
        self.heading.pack()
        self.prompt.pack(anchor=tk.W, pady=10)
        self.entry.pack(fill="x", pady=10)
        self.response.pack(expand=True)
        self.buttongrid.pack()
        self.check_btn.pack(side=tk.LEFT)
        self.show_btn.pack(side=tk.LEFT)
        self.next_btn.pack(side=tk.LEFT)

    def _check_answer(self):
        if self.currquestion.check_answer(self.inputvar.get()):
            self.response["text"] = "Correct!"
        else:
            self.response["text"] = "Incorrect."

    def _show_answer(self):
        self.response["text"] = f"The correct answer is {self.currquestion.answer}."

    def _next_question(self):
        self.currquestion = self.qgen()
        self.prompt["text"] = self.currquestion.prompt
        self.inputvar.set("")
        self.response["text"] = "Enter your answer."


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(400, 300)
    root.maxsize(400, 300)
    style = ttk.Style()
    style.theme_use("clam")
    app = Gui()
    root.mainloop()
