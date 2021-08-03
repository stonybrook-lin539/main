"""
Data structures for question formats.
"""

class Question:
    """
    Abstract base class for question.
    """

    def __init__(self, prompt, promptfigure=None):
        """
        prompt - string, possibly multiline
        promptfigure - png image
        """
        self.prompt = prompt
        self.promptfigure = promptfigure

    def check_answer(self, answer):
        """Return True if answer matches correct answer."""
        raise NotImplementedError("Method must be implemented by subclass.")

    # def formatted_answer(self):
    #     """Return string form of correct answer."""
    #     raise NotImplementedError("Method must be implemented by subclass.")


class FreeResponseQuestion(Question):
    """
    A free response question provides no answer choices. The student enters
    the answer using the keyboard.
    """

    answertypes = ("string", "integer")

    def __init__(self, prompt, answer, answertype="string", promptfigure=None):
        super().__init__(prompt, promptfigure)
        if answertype not in self.answertypes:
            raise ValueError(
                f"Parameter 'answertype' must be one of {self.answertypes}.")
        elif answertype == "string" and not isinstance(answer, str):
            raise ValueError(
                f"Parameter 'answer' is not a string, as specified.")
        elif answertype == "integer" and not isinstance(answer, int):
            raise ValueError(
                f"Parameter 'answer' is not an integer, as specified.")
        self.prompt = prompt
        self.answer = answer
        self.answertype = answertype

    def __str__(self):
        return (
            f"<FreeInputQuestion>"
            f"\nPrompt: {self.prompt}"
            f"\nAnswer: {self.answer}")

    def check_answer(self, studentanswer):
        if self.answertype == "string":
            if not isinstance(studentanswer, str):
                raise ValueError(
                    f"Expecting input of type 'str'.")
            return studentanswer == self.answer
        elif self.answertype == "integer":
            if not isinstance(studentanswer, int):
                raise ValueError(
                    f"Expecting input of type 'int'.")
            return studentanswer == self.answer


class ListResponseQuestion(Question):
    """
    A list response question is similar to a free response question. The
    student is asked to enter all answers that apply, e.g. separated by commas.
    """

    def __init__(self, prompt, answer, promptfigure=None):
        super().__init__(prompt, promptfigure)
        if (not isinstance(answer, list)
                or not all(isinstance(e, str) for e in answer)):
            raise ValueError(
                "Parameter 'answer' must be a list of strings.")
        self.prompt = prompt
        self.answer = answer

    def __str__(self):
        return (
            f"<ListReponseQuestion>"
            f"\nPrompt: {self.prompt}"
            f"\nAnswer: {self.answer}")

    def check_answer(self, studentanswer):
        if (not isinstance(studentanswer, list)
                or not all(isinstance(e, str) for e in studentanswer)):
            raise ValueError(
                "Expecting a list of strings.")
        return sorted(studentanswer) == sorted(self.answer)


class MultipleChoiceQuestion(Question):
    """
    A multiple choice question provides several answer choices and asks the
    student to select one.
    """

    def __init__(self, prompt, choices, answeridx, promptfigure=None):
        super().__init__(prompt, promptfigure)
        if (not isinstance(choices, list)
                or not all(isinstance(e, str) for e in choices)):
            raise ValueError(
                "Parameter 'choices' must be a list of strings.")
        self.prompt = prompt
        self.choices = choices
        self.answeridx = answeridx

    def __str__(self):
        return (
            f"<MultipleChoiceQuestion>"
            f"\nPrompt: {self.prompt}"
            f"\nChoices: {str(list(enumerate(self.choices)))}"
            f"\nAnswer: {self.answeridx}")

    def check_answer(self, inputidx):
        if inputidx not in range(len(self.choices)):
            raise ValueError("Index out of range.")
        return inputidx == self.answeridx

    def correct_answer(self):
        return self.choices[self.answeridx]


class MultipleAnswerQuestion(Question):
    """
    A multiple answer question is similar to a multiple choice question. The
    student is asked to select all answers that apply.
    """

    def __init__(self, prompt, choices, answeridxlst, promptfigure=None):
        super().__init__(prompt, promptfigure)
        if (not isinstance(choices, list)
                or not all(isinstance(e, str) for e in choices)):
            raise ValueError(
                "Parameter 'choices' must be a list of strings.")
        self.prompt = prompt
        self.choices = choices
        self.answeridxlst = answeridxlst

    def __str__(self):
        return (
            f"<MultipleChoiceQuestion>"
            f"\nPrompt: {self.prompt}"
            f"\nChoices: {str(list(enumerate(self.choices)))}"
            f"\nAnswer: {self.answeridxlst}")

    def check_answer(self, inputidxlst):
        for i in inputidxlst:
            if i not in range(len(self.choices)):
                raise ValueError("Index out of range.")
        return sorted(inputidxlst) == sorted(self.answeridxlst)

    def correct_answer(self):
        return str(self.answeridxlst)


if __name__ == "__main__":
    frq = FreeResponseQuestion(
        "What is the answer?",
        "lizard",
        "string")
    print(frq)
    print()

    for a in ("lizard", "Lizard", "snake", 3):
        try:
            print(a, "---", frq.check_answer(a))
        except Exception as e:
            print(a, "---", e)
    print()

    mcq = MultipleChoiceQuestion(
        "Which is the smallest?",
        ["cat", "dog", "mouse"],
        2)
    print(mcq)
    print()

    for a in (0, 1, 2, 3):
        try:
            print(a, "---", mcq.check_answer(a))
        except Exception as e:
            print(a, "---", e)
    print()

    maq = MultipleAnswerQuestion(
        "Which is delicious?",
        ["pie", "beef", "squid"],
        [0, 1])
    print(maq)
    print()

    from util import powerset
    for a in powerset(range(3)):
        try:
            print(a, "---", maq.check_answer(a))
        except Exception as e:
            print(a, "---", e)
    print()
