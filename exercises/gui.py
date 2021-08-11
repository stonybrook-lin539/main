#!/usr/bin/env python3

"""
Prototype GUI for LIN 539 interactive exercises.
"""

import tkinter as tk
from tkinter import ttk
import PIL.ImageTk

import question as qu
import questiongen as qgen


question_categories = {
    "Logic": {
        "Logic Op Result": qgen.logic.logic_op_result,
        "Logic Two Op Result": qgen.logic.logic_2op_result,
        "Which Logic Op": qgen.logic.which_logic_op
    },
    "Sets": {
        "Set Op Result": qgen.sets.set_op_result,
        "Set Two Op Result": qgen.sets.set_2op_result,
        "Which Set Op": qgen.sets.which_set_op,
        "Which Set Relation": qgen.sets.which_set_relation
    },
    "Functions": {
        "Function to Monotonicity": qgen.functions.func_to_monotonicity,
        "Monotonicity to Function": qgen.functions.monotonicity_to_function
    },
    "Relations": {
        "Relation Properties": qgen.relations.relation_props
    },
    "Strings": {
        "List Substrings": qgen.strings.list_substr_length_k,
        "List Subsequences": qgen.strings.list_subseq_length_k
    },
    "N-grams": {
        "Matching Strings": qgen.ngrams.choose_matching_strings
    },
    "FSAs": {
        "FSA to Language": qgen.fsas.fsa_to_language,
        "Language to FSA": qgen.fsas.language_to_fsa
    }
}


class Gui(ttk.Frame):
    """
    Parent application. Controls question type selection.
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.qgen = None
        self.qtypevar = tk.StringVar()
        self._init_ui()

    def _init_ui(self):
        topwindow = self.winfo_toplevel()
        self.menubar = tk.Menu(topwindow)
        topwindow["menu"] = self.menubar

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
        self.questionwidget = qwidgettype(self, qtype, qgen)
        self.questionwidget.pack(fill="both", padx=10, pady=10)


class QuestionWidget(ttk.Frame):
    """
    Base class for widget that displays a question and accepts user input.
    Each question type must be implemented as a subclass.
    """

    instruction_text = "Enter your answer."

    def __init__(self, parent, qtype, qgen):
        """
        qtype -- string, used to create heading
        qgen -- question generator function
        """
        super().__init__(parent)
        self.qtype = qtype
        self.qgen = qgen
        self._init_ui()
        self._load_question()

    def _init_ui(self):
        """Create widgets and configure layout."""
        self.heading = ttk.Label(self, text=self.qtype)
        # self.helpbutton = ttk.Button(self, text="Help", padding=0, width=0)
        self.prompt = ttk.Label(self, wraplength=480)
        self.promptfigure = ttk.Label(self)
        self.answerwidget = ttk.Frame(self)
        self.response = ttk.Label(self)

        self.buttonlayout = ttk.Frame(self)
        self.check_btn = ttk.Button(self.buttonlayout,
                                    text="Check Answer",
                                    command=self._check_answer)
        self.show_btn = ttk.Button(self.buttonlayout,
                                   text="Show Answer",
                                   command=self._show_answer)
        self.next_btn = ttk.Button(self.buttonlayout,
                                   text="Next Question",
                                   command=self._load_question)

        # place everything except promptfigure, which is only needed for
        #   questions with a figure
        self.heading.pack()
        # self.helpbutton.place(relx=1.0, rely=0.0, anchor=tk.NE)
        self.prompt.pack(anchor=tk.W)
        self.answerwidget.pack(anchor=tk.W, fill="x")
        self.response.pack(anchor=tk.W)
        self.buttonlayout.pack()
        self.check_btn.pack(side=tk.LEFT)
        self.show_btn.pack(side=tk.LEFT)
        self.next_btn.pack(side=tk.LEFT)

    def _check_answer(self):
        """Inform user whether the current answer is correct."""
        if self._answer_is_correct():
            self.response["text"] = "Correct!"
        else:
            self.response["text"] = "Incorrect."

    def _answer_is_correct(self):
        """Process user input and compare to correct answer.
        Must be implemented by subclass."""
        raise NotImplementedError("Method must be implemented by subclass.")

    def _show_answer(self):
        """Show correct answer for the current question.
        Must be implemented by subclass."""
        raise NotImplementedError("Method must be implemented by subclass.")

    def _load_question(self):
        """
        Generate and display a question. Called at initialization, and whenever
        a new question of the same type is to be loaded. Should be extended by
        subclass to (re)initialize answer widget.
        """
        self.question = self.qgen()
        self.prompt["text"] = self.question.prompt
        self.response["text"] = self.instruction_text
        if self.question.promptfigure is not None:
            # keep reference to the PhotoImage to prevent garbage collection
            self.image = PIL.ImageTk.PhotoImage(self.question.promptfigure)
            self.promptfigure["image"] = self.image
            self.promptfigure.pack(after=self.prompt)


class FreeResponseWidget(QuestionWidget):

    instruction_text = "Enter your answer in the text box."

    def _init_ui(self):
        self._init_ui()
        self.answervar = tk.StringVar()
        self.entry = ttk.Entry(self.answerwidget, textvariable=self.answervar)
        self.entry.pack()

    def _answer_is_correct(self):
        return self.question.check_answer(self.answervar.get().strip())

    def _show_answer(self):
        self.response["text"] = f"The correct answer is {self.question.answer}."

    def _load_question(self):
        super()._load_question()
        self.answervar.set("")


class ListResponseWidget(QuestionWidget):

    instruction_text = "Enter your answers separated by commas."

    def _init_ui(self):
        super()._init_ui()
        self.answervar = tk.StringVar()
        self.entry = ttk.Entry(self.answerwidget, textvariable=self.answervar)
        self.entry.pack()

    def _answer_is_correct(self):
        anslist = [e.strip() for e in self.answervar.get().split(',')]
        return self.question.check_answer(anslist)

    def _show_answer(self):
        self.response["text"] = f"The correct answer is {self.question.answer}."

    def _load_question(self):
        super()._load_question()
        self.answervar.set("")


class MultipleChoiceWidget(QuestionWidget):

    instruction_text = "Select your answer."

    def _init_ui(self):
        super()._init_ui()
        self.answervar = tk.IntVar()
        self.radio_btns = []

    def _answer_is_correct(self):
        return self.question.check_answer(self.answervar.get())

    def _show_answer(self):
        if self.question.answertype == "string":
            answer = f"({self.question.answeridx + 1}) {self.question.correct_answer()}"
        elif self.question.answertype == "image":
            answer = f"({self.question.answeridx + 1})"
        self.response["text"] = f"The correct answer is {answer}."

    def _load_question(self):
        super()._load_question()
        for b in self.radio_btns:
            b.pack_forget()
        if self.question.answertype == "string":
            self.radio_btns = [
                ttk.Radiobutton(self.answerwidget,
                                text=f"({idx + 1}) {text}",
                                variable=self.answervar,
                                value=idx)
                for idx, text in enumerate(self.question.choices)]
        elif self.question.answertype == "image":
            # keep references to the PhotoImages to prevent garbage collection
            self.answer_images = [PIL.ImageTk.PhotoImage(img)
                                  for img in self.question.choices]
            self.radio_btns = [
                ttk.Radiobutton(self.answerwidget,
                                image=img,
                                variable=self.answervar,
                                value=idx)
                for idx, img in enumerate(self.answer_images)]
        for b in self.radio_btns:
            b.pack(anchor=tk.W)


class MultipleAnswerWidget(QuestionWidget):

    instruction_text = "Select all answers that apply."

    def _init_ui(self):
        super()._init_ui()
        self.answervar = tk.Variable()
        self.answervars = []
        self.check_btns = []

    def _answer_is_correct(self):
        return self.question.check_answer(
            [i for i, var in enumerate(self.answervars) if var.get() == 1])

    def _show_answer(self):
        answer = str([idx + 1 for idx in self.question.answeridxlst])
        self.response["text"] = f"The correct answer is {answer}."

    def _load_question(self):
        super()._load_question()
        for b in self.check_btns:
            b.pack_forget()
        self.answervars = [tk.IntVar() for c in self.question.choices]
        if self.question.answertype == "string":
            self.check_btns = [
                ttk.Checkbutton(self.answerwidget,
                                text=f"({idx + 1}) {text}",
                                variable=self.answervars[idx])
                for idx, text in enumerate(self.question.choices)]
        elif self.question.answertype == "image":
            # keep references to the PhotoImages to prevent garbage collection
            self.answer_images = [PIL.ImageTk.PhotoImage(img)
                                  for img in self.question.choices]
            self.check_btns = [
                ttk.Checkbutton(self.answerwidget,
                                image=img,
                                variable=self.answervars[idx])
                for idx, img in enumerate(self.answer_images)]
        for b in self.check_btns:
            b.pack(anchor=tk.W)


question_widgets = {
    qu.FreeResponseQuestion: FreeResponseWidget,
    qu.ListResponseQuestion: ListResponseWidget,
    qu.MultipleChoiceQuestion: MultipleChoiceWidget,
    qu.MultipleAnswerQuestion: MultipleAnswerWidget
}


def set_style():
    """Must be called after creating root widget."""
    style = ttk.Style()
    style.theme_use("clam")

    # add a little vertical space between widgets
    style.configure('.', padding="0 5")

    # add moderate indentation to radio buttons and checkboxes
    style.configure('TRadiobutton', padding="10 0")
    style.configure('TCheckbutton', padding="10 0")


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(480, 320)
    set_style()
    app = Gui(root)
    root.mainloop()
