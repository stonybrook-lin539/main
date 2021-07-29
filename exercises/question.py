

class FreeResponseQuestion:
    answertypes = ("string", "integer")

    def __init__(self, prompt, answer, answertype="string"):
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

    def check_answer(self, userinput):
        if self.answertype == "string":
            if not isinstance(userinput, str):
                raise ValueError(
                    f"Expecting input of type 'str'.")
            cleaninput = userinput.strip().lower()
            return cleaninput == self.answer
        elif self.answertype == "integer":
            if not isinstance(userinput, int):
                raise ValueError(
                    f"Expecting input of type 'int'.")
            return cleaninput == self.answer


class MultipleChoiceQuestion:

    def __init__(self, prompt, choices, answeridx):
        if (not isinstance(choices, list)
                or not all(isinstance(e, str) for e in choices)):
            raise ValueError(
                f"Parameter 'choices' is not a list of strings, as specified.")
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


class MultipleAnswerQuestion:

    def __init__(self, prompt, choices, answeridxlst):
        if (not isinstance(choices, list)
                or not all(isinstance(e, str) for e in choices)):
            raise ValueError(
                f"Parameter 'choices' is not a list of strings, as specified.")
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
