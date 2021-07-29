"""
Prototype GUI for LIN 539 interactive exercises.
"""

import tkinter as tk
from tkinter import ttk

import question as qu
import questiongen as qgen


question_types = {
    "sets": {
        "Set Op Result": qgen.sets.set_op_result,
        "Set Two Op Result": qgen.sets.set_2op_result,
        "Which Set Op": qgen.sets.which_set_op,
        "Which Set Relation": qgen.sets.which_set_relation,
    },
    "strings": {
        "List Substrings": qgen.strings.list_substr_length_k,
        "List Subsequences": qgen.strings.list_subseq_length_k
    }
}


class Gui(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.qgen = qgen.sets.which_set_relation
        self._init_ui()

    def _init_ui(self):
        # topwindow = self.winfo_toplevel()
        # self.menubar = tk.Menu(topwindow)
        # topwindow["menu"] = self.menubar
        # for i in range(5):
        #     self.menubar.add_command(label='Show Answer', command=self._show_answer)

        qwidgettype = question_widgets[type(self.qgen())]
        self.questionwidget = qwidgettype(self, self.qgen)

        self.pack(fill="both", expand=True)
        self.questionwidget.pack()


class QuestionWidget(ttk.Frame):

    def __init__(self, parent, qgen):
        super().__init__(parent)
        self.qgen = qgen
        self.question = qgen()
        self._init_ui()

    def _init_ui(self):
        self.heading = ttk.Label(self, text="Set Question")
        self.prompt = ttk.Label(self, text=self.question.prompt, wraplength=600)
        self.answerwidget = ttk.Frame(self)
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
                                   command=self._load_question)

        self.heading.pack()
        self.prompt.pack(anchor=tk.W, pady=10)
        self.answerwidget.pack(anchor=tk.W, fill="x", pady=10)
        self.response.pack(expand=True)
        self.buttongrid.pack()
        self.check_btn.pack(side=tk.LEFT)
        self.show_btn.pack(side=tk.LEFT)
        self.next_btn.pack(side=tk.LEFT)

    def _check_answer(self):
        if self.question.check_answer(self.val.get()):
            self.response["text"] = "Correct!"
        else:
            self.response["text"] = "Incorrect."

    def _show_answer(self):
        raise NotImplementedError("Method must be implemented by subclass.")

    def _load_question(self):
        self.question = self.qgen()
        self.prompt["text"] = self.question.prompt
        self.val.set("")
        self.response["text"] = "Enter your answer."


class FreeResponseWidget(QuestionWidget):

    def __init__(self, parent, qgen):
        super().__init__(parent, qgen)
        self.val = tk.StringVar()
        self._init_answer_ui()

    def _init_answer_ui(self):
        self.entry = ttk.Entry(self.answerwidget, textvariable=self.val)
        self.entry.pack()

    def _show_answer(self):
        self.response["text"] = f"The correct answer is {self.question.answer}."

    def _load_question(self):
        super()._load_question()
        self._init_answer_ui()


class ListResponseWidget(QuestionWidget):
    pass


class MultipleChoiceWidget(QuestionWidget):

    def __init__(self, parent, qgen):
        super().__init__(parent, qgen)
        self.val = tk.IntVar()
        self._init_answer_ui()

    def _init_answer_ui(self):
        self.radio_btns = [
            ttk.Radiobutton(self.answerwidget,
                            text=f"({idx + 1}) {text}",
                            variable=self.val,
                            value=idx)
            for idx, text in enumerate(self.question.choices)]
        for b in self.radio_btns:
            b.pack(anchor=tk.W)

    def _show_answer(self):
        answer = f"({self.question.answeridx + 1}) {self.question.correct_answer()}"
        self.response["text"] = f"The correct answer is {answer}."

    def _load_question(self):
        super()._load_question()
        for b in self.radio_btns:
            b.pack_forget()
        self._init_answer_ui()


class MultipleAnswerWidget(QuestionWidget):
    pass


question_widgets = {
    qu.FreeResponseQuestion: FreeResponseWidget,
    qu.ListResponseQuestion: ListResponseWidget,
    qu.MultipleChoiceQuestion: MultipleChoiceWidget,
    qu.MultipleAnswerQuestion: MultipleAnswerWidget
}


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(600, 400)
    # root.maxsize(400, 300)
    style = ttk.Style()
    style.theme_use("clam")
    app = Gui(root)
    root.mainloop()
