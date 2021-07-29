import tkinter as tk
from tkinter import ttk


import questiongen as qgen


class Gui(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.qgen = qgen.which_set_relation
        self.currquestion = self.qgen()
        self._init_ui()

    def _init_ui(self):
        self.heading = ttk.Label(self, text="Set Question")
        self.prompt = ttk.Label(self, text=self.currquestion.prompt, wraplength=600)
        self.answerwidget = MultipleChoiceWidget(self, self.currquestion.choices)
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

        self.pack(fill="both", expand=True, padx=10, pady=10)
        self.heading.pack()
        self.prompt.pack(anchor=tk.W, pady=10)
        self.answerwidget.pack(anchor=tk.W, fill="x", pady=10)
        self.response.pack(expand=True)
        self.buttongrid.pack()
        self.check_btn.pack(side=tk.LEFT)
        self.show_btn.pack(side=tk.LEFT)
        self.next_btn.pack(side=tk.LEFT)

    def _check_answer(self):
        if self.currquestion.check_answer(self.answerwidget.val.get()):
            self.response["text"] = "Correct!"
        else:
            self.response["text"] = "Incorrect."

    def _show_answer(self):
        self.response["text"] = f"The correct answer is {self.currquestion.answer}."

    def _next_question(self):
        self.currquestion = self.qgen()
        self.prompt["text"] = self.currquestion.prompt
        self.answerwidget.val.set("")
        self.response["text"] = "Enter your answer."


class FreeResponseWidget(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.val = tk.StringVar()
        self._init_ui()

    def _init_ui(self):
        self.entry = ttk.Entry(self, textvariable=self.val)
        self.entry.pack()


class MultipleChoiceWidget(ttk.Frame):

    def __init__(self, parent, entries):
        super().__init__(parent)
        self.entries = entries
        self.val = tk.IntVar()
        self._init_ui()

    def _init_ui(self):
        self.radio_btns = [
            ttk.Radiobutton(self, text=text, variable=self.val, value=idx)
            for idx, text in enumerate(self.entries)]
        for b in self.radio_btns:
            b.pack(anchor=tk.W)


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(600, 400)
    # root.maxsize(400, 300)
    style = ttk.Style()
    style.theme_use("clam")
    app = Gui(root)
    root.mainloop()
