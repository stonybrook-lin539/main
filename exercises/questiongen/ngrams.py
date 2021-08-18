"""
Question generators for strings.
"""

import string
import random

from util import random_string, language_sigma_k
import question
import grammars


def choose_matching_strings(alpha_size=3, ngram_size=3, ngram_num=6,
                            str_size=8, n_choices=6):
    """
    Generate question asking student to select all strings that conform
    to the given grammar.

    We generate a random n-gram grammar, then randomly generate some strings
    that conform to the grammar and some that don't. There is a small chance
    that some of the "bad" strings may also conform to the grammar, but this
    isn't a problem because we later shuffle the list of choices and recheck
    them to generate the list of correct answers.
    """
    alphabet = string.ascii_lowercase[:alpha_size]
    grammar_type = random.choice(["positive", "negative"])
    grammar_gen = GRAMMAR_TYPES[grammar_type]
    mygrammar = grammar_gen(alphabet, ngram_size, ngram_num, str_size)

    n_good_choices = random.randrange(n_choices)
    choices = mygrammar.gen_strings_fast(str_size, n_good_choices, randomize=True)
    while len(choices) < n_choices:
        newchoice = random_string(alphabet, random.randrange(str_size + 1))
        if newchoice not in choices:
            choices.append(newchoice)
    random.shuffle(choices)

    prompt = (
        "Select all strings that conform to the following n-gram grammar:"
        f"\n  {mygrammar}")
    answers = [i for i, c in enumerate(choices) if mygrammar.match(c)]
    return question.MultipleAnswerQuestion(prompt, choices, answers)


def _random_positive_grammar(alphabet, ngram_size, ngram_num, str_size):
    """
    Randomly generate some strings, then build grammar from this corpus.
    """
    corpus = [random_string(alphabet, str_size)]
    for i in range(ngram_size):
        if random.getrandbits(1):
            corpus.append(random_string(alphabet, i))
    return grammars.PosNGramGrammar.from_corpus(alphabet, ngram_size, corpus)


def _random_negative_grammar(alphabet, ngram_size, ngram_num, str_size):
    """
    Randomly generate some n-grams, then build grammar from these.
    """
    ngrams = random.sample(language_sigma_k(alphabet, ngram_size), ngram_num)
    return grammars.NegNGramGrammar(alphabet, ngram_size, ngrams)


GRAMMAR_TYPES = {"positive": _random_positive_grammar,
                 "negative": _random_negative_grammar}


def test():
    q = choose_matching_strings()
    print(q)


if __name__ == "__main__":
    test()
