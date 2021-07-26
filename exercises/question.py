class FreeInputQuestion:
    answertypes = ("string", "stringlist")

    def __init__(self, prompt, answer, answertype="string"):
        if answertype not in self.answertypes:
            raise ValueError(
                f"Parameter 'answertype' must be one of {self.answertypes}.")
        elif answertype == "string" and not isinstance(answer, str):
            raise ValueError(
                f"Parameter 'answer' is not a string, as specified.")
        elif answertype == "stringlist" and (
                not isinstance(answer, list)
                or not all(isinstance(e, str) for e in answer)):
            raise ValueError(
                f"Parameter 'answer' is not a list of strings, as specified.")
        self.prompt = prompt
        self.answer = answer
        self.answertype = answertype

    def __str__(self):
        return (
            f"<Question>\n"
            f"{self.prompt}\n"
            f"Answer: {self.answer}\n")

    def terminal_format(self):
        pass

    def check_answer(self, userinput):
        if self.answertype == "string":
            if not isinstance(userinput, str):
                raise ValueError(
                    f"Expecting input of type 'str'.")
            cleaninput = userinput.strip().lower()
            return cleaninput == self.answer
        elif self.answertype == "stringlist":
            if not isinstance(userinput, list):
                raise ValueError(
                    f"Expecting input of type 'list'.")
            cleaninput = userinput.strip().lower()
            parsedinput = cleaninput.split(',')
            return all(user == answer
                       for user, answer in zip(parsedinput, self.answer))

    # __repr__ = __str__


if __name__ == "__main__":
    q = FreeInputQuestion("What is the answer?",
                          "lizard",
                          "string")
    for a in ("lizard", "Lizard", "snake", 3):
        try:
            print(q.check_answer(a))
        except Exception:
            print("Error")
