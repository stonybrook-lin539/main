"""
Prototype GUI for LIN 539 interactive exercises.
"""

import tkinter as tk
from tkinter import ttk

import question as qu
import questiongen as qgen


question_categories = {
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
        self.qgen = None
        self.qtypevar = tk.StringVar()
        self._init_ui()

    def _init_ui(self):
        topwindow = self.winfo_toplevel()
        self.menubar = tk.Menu(topwindow)
        topwindow["menu"] = self.menubar

        # setmenu = tk.Menu()
        # stringmenu = tk.Menu()
        # self.menubar.add_cascade(label="Sets", menu=setmenu)
        # self.menubar.add_cascade(label="Strings", menu=stringmenu)

        for qcat in question_categories:
            catmenu = tk.Menu(self.menubar, tearoff=False)
            self.menubar.add_cascade(label=qcat, menu=catmenu)
            qtypes = question_categories[qcat]
            for qtype in qtypes:
                catmenu.add_radiobutton(
                    label=qtype,
                    command=self._select_qtype,
                    variable=self.qtypevar,
                    value=f"{qcat}/{qtype}")

        self.questionwidget = ttk.Label(self,
                                        text="Please select a question type.")

        self.pack(fill="both", expand=True)
        self.questionwidget.pack(expand=True)

    def _select_qtype(self):
        qcat, qtype = self.qtypevar.get().split('/')
        qgen = question_categories[qcat][qtype]
        qwidgettype = question_widgets[type(qgen())]

        self.questionwidget.pack_forget()
        self.questionwidget = qwidgettype(self, qgen)
        self.questionwidget.pack(fill="x", expand=True, padx=10, pady=10)


class QuestionWidget(ttk.Frame):

    instruction_text = "Enter your answer."

    def __init__(self, parent, qgen):
        super().__init__(parent)
        self.qgen = qgen
        self.question = qgen()
        self._init_ui()

    def _init_ui(self):
        self.heading = ttk.Label(self, text="Set Question")
        self.prompt = ttk.Label(self, text=self.question.prompt, wraplength=480)
        self.answerwidget = ttk.Frame(self)
        self.response = ttk.Label(self, text=self.instruction_text)

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
        self.response.pack(anchor=tk.W, expand=True, pady=10)
        self.buttongrid.pack()
        self.check_btn.pack(side=tk.LEFT)
        self.show_btn.pack(side=tk.LEFT)
        self.next_btn.pack(side=tk.LEFT)

    def _is_correct_answer(self):
        raise NotImplementedError("Method must be implemented by subclass.")

    def _check_answer(self):
        if self._is_correct_answer():
            self.response["text"] = "Correct!"
        else:
            self.response["text"] = "Incorrect."

    def _show_answer(self):
        raise NotImplementedError("Method must be implemented by subclass.")

    def _load_question(self):
        self.question = self.qgen()
        self.prompt["text"] = self.question.prompt
        self.response["text"] = self.instruction_text


class FreeResponseWidget(QuestionWidget):

    def __init__(self, parent, qgen):
        super().__init__(parent, qgen)
        self.val = tk.StringVar()
        self._init_answer_ui()

    def _init_answer_ui(self):
        self.entry = ttk.Entry(self.answerwidget, textvariable=self.val)
        self.entry.pack()

    def _is_correct_answer(self):
        return self.question.check_answer(self.val.get().strip())

    def _show_answer(self):
        self.response["text"] = f"The correct answer is {self.question.answer}."

    def _load_question(self):
        super()._load_question()
        self.val.set("")


class ListResponseWidget(QuestionWidget):

    instruction_text = "Enter your answers separated by commas."

    def __init__(self, parent, qgen):
        super().__init__(parent, qgen)
        self.val = tk.StringVar()
        self._init_answer_ui()

    def _init_answer_ui(self):
        self.entry = ttk.Entry(self.answerwidget, textvariable=self.val)
        self.entry.pack()

    def _is_correct_answer(self):
        anslist = [e.strip() for e in self.val.get().split(',')]
        return self.question.check_answer(anslist)

    def _show_answer(self):
        self.response["text"] = f"The correct answer is {self.question.answer}."

    def _load_question(self):
        super()._load_question()
        self.val.set("")


class MultipleChoiceWidget(QuestionWidget):

    instruction_text = "Select your answer."

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
            b.pack(anchor=tk.W, padx=20)

    def _is_correct_answer(self):
        return self.question.check_answer(self.val.get())

    def _show_answer(self):
        answer = f"({self.question.answeridx + 1}) {self.question.correct_answer()}"
        self.response["text"] = f"The correct answer is {answer}."

    def _load_question(self):
        super()._load_question()
        for b in self.radio_btns:
            b.pack_forget()
        self._init_answer_ui()


class MultipleAnswerWidget(QuestionWidget):

    instruction_text = "Select each item that applies."

    def __init__(self, parent, qgen):
        super().__init__(parent, qgen)
        self._init_answer_ui()

    def _init_answer_ui(self):
        choices = [f"({idx + 1}) {text}"
                   for idx, text in enumerate(self.question.choices)]
        self.val = tk.Variable(value=choices)
        self.listbox = tk.Listbox(self.answerwidget,
                                  listvariable=self.val,
                                  selectmode=tk.MULTIPLE,
                                  height=len(choices))
        self.listbox.pack()

    def _is_correct_answer(self):
        return self.question.check_answer(self.listbox.curselection())

    def _show_answer(self):
        answer = str([idx + 1 for idx in self.question.answeridxlst])
        self.response["text"] = f"The correct answer is {answer}."

    def _load_question(self):
        super()._load_question()
        self.listbox.pack_forget()
        self._init_answer_ui()


question_widgets = {
    qu.FreeResponseQuestion: FreeResponseWidget,
    qu.ListResponseQuestion: ListResponseWidget,
    qu.MultipleChoiceQuestion: MultipleChoiceWidget,
    qu.MultipleAnswerQuestion: MultipleAnswerWidget
}


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(480, 320)
    style = ttk.Style()
    style.theme_use("clam")
    app = Gui(root)
    root.mainloop()
