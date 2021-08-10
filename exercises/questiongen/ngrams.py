"""
Question generators for strings.
"""

import string
import random
import math

from util import language_random_subset
import question
import grammars


def choose_matching_strings(alpha_size=3, ngram_size=3, ngram_num=6,
                            str_size=8, n_choices=6):
    """
    Generate question asking student to select all strings that conform
    to the given grammar.

    We generate a random ngram grammar, then randomly generate some strings
    that conform to the grammar and some that don't. There is a small chance
    that some of the "bad" strings may also conform to the grammar, but this
    isn't a problem because we later shuffle the list of choices and recheck
    them to generate the list of correct answers.
    """
    alphabet = string.ascii_lowercase[:alpha_size]
    grammar_type = random.choice(["positive", "negative"])
    grammar_gen = GRAMMAR_TYPES[grammar_type]
    # grammar_gen = random_positive_grammar
    mygrammar = grammar_gen(alphabet, ngram_size, ngram_num, str_size)

    n_good_choices = random.randrange(n_choices)
    n_bad_choices = n_choices - n_good_choices
    good_choices = mygrammar.gen_strings_fast(str_size, n_good_choices, randomize=True)
    bad_choices = language_random_subset(alphabet, str_size, n_bad_choices)

    choices = [*good_choices, *bad_choices]
    random.shuffle(choices)

    prompt = (
        "Select all strings that conform to the following n-gram grammar:"
        f"\n  {mygrammar}")
    answers = [i for i, c in enumerate(choices) if mygrammar.match(c)]
    return question.MultipleAnswerQuestion(prompt, choices, answers)


def random_positive_grammar(alphabet, ngram_size, ngram_num, str_size):
    """
    Randomly generate some n-grams, then add additional n-grams to ensure
    that strings of the specified size can be generated.
    """
    ngrams = language_random_subset(alphabet, ngram_size, ngram_num)
    extra_ngrams = []
    # select enough n-grams that when concatenated would be long enough
    for i in range(math.ceil(str_size / ngram_size) - 1):
        ng1, ng2 = ngrams[i:i+2]
        # add the missing intermediate n-grams
        for j in range(1, ngram_size):
            extra = ng1[j:] + ng2[:j]
            extra_ngrams.append(extra)
    ngrams.extend(extra_ngrams)
    return grammars.PosNGramGrammar(alphabet, ngram_size, ngrams)


def random_negative_grammar(alphabet, ngram_size, ngram_num, str_size):
    """
    Randomly generate some n-grams. Unlike with a positive grammar, no further
    modifications are needed.
    """
    ngrams = language_random_subset(alphabet, ngram_size, ngram_num)
    return grammars.NegNGramGrammar(alphabet, ngram_size, ngrams)


GRAMMAR_TYPES = {"positive": random_positive_grammar,
                 "negative": random_negative_grammar}


if __name__ == "__main__":
    print(choose_matching_strings())
