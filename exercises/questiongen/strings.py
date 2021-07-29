import random

from util import substrings_len_k_of, subsequences_len_k_of
import question


STROPS = {"concat": str.__add__,
          "substr": str.__contains__,
          "strictsubstr": lambda x, y: x in y and not x == y,
          "equal": str.__eq__}
STRSYMS = {"concat": '·',
           "substr": '⊑',
           "strictsubstr": '⊏',
           "equal": "="}

STRSET_SAMPLE = ("blue", "berry", "blueberry", "bluebird", "bird")


def list_substr_length_k():
    alphabet = "abcd"
    mystr = ''.join(random.choices(alphabet, k=5))
    k = random.choice(range(len(mystr) + 1))

    substrs = substrings_len_k_of(mystr, k=k)
    prompt = f"List all substrings of length {k} of the string '{mystr}'."
    answer = substrs
    return question.ListResponseQuestion(prompt, answer)


def list_subseq_length_k():
    alphabet = "abcd"
    mystr = ''.join(random.choices(alphabet, k=5))
    k = random.choice(range(len(mystr) + 1))

    substrs = subsequences_len_k_of(mystr, k=k)
    prompt = f"List all subsequences of length {k} of the string '{mystr}'."
    answer = substrs
    return question.ListResponseQuestion(prompt, answer)


if __name__ == "__main__":
    for i in range(10):
        print(list_subseq_length_k(), end="\n\n")
