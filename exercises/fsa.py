#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Provides FSA for strings. Based on Kenneth's code from LIN 637.
"""

import copy
from itertools import product
import operator

import pydot


class FSA:
    """Deterministic finite-state acceptor for strings.

    Parameters
    ----------
    alphabet: a finite set of symbols that form the alphabet
    states: a finite set of states
    initial: initial state
    finals: set of final states
    transtitions: a dictionary of the form {(from_state, input_symbol): to_state}

    All sets may be alternatively provided as lists, in which case they will
    be converted automatically. The transition dictionary may likewise be
    provided as a set or list of tuples.
    """

    def __init__(self, states, alphabet, initial, finals, transitions):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.initial = initial
        self.finals = set(finals)

        if type(transitions) in (set, list):
            self.transitions = self._delta_dict(transitions)
        elif type(transitions) == dict:
            self.transitions = transitions

    def __str__(self):
        return ("<FSA>\n"
                f"states: {self.states}\n"
                f"alphabet: {self.alphabet}\n"
                f"initial: {self.initial}\n"
                f"finals: {self.finals}\n"
                f"transitions: {self.transitions}")

    def to_pydot(self):
        g = pydot.Dot("fsa", graph_type="digraph", rankdir="LR")
        g.set_graph_defaults(nodesep=0.15)
        g.set_node_defaults(height=.3, fontsize=10, margin="0.0,0.0")
        g.set_edge_defaults(fontsize=10, arrowsize=0.5)
        for state in self.states:
            shape = "doublecircle" if state in self.finals else "circle"
            g.add_node(pydot.Node(state, shape=shape))

        # merge edges between same pair of node into one edge with compound label
        edges = {}
        for ((state, sym), nextstate) in self.transitions.items():
            if (state, nextstate) not in edges:
                edges[state, nextstate] = [sym]
            else:
                edges[state, nextstate].append(sym)
        for ((state, nextstate), syms) in edges.items():
            g.add_edge(pydot.Edge(state, nextstate, label='\\,'.join(syms)))
        return g

    def _delta_dict(self, transitions):
        """Convert transition list of form (state, symbol, nextstate)
        to dictionary of form {(state, symbol): nextstate}."""
        return {(state, symbol): nextstate
                for (state, symbol, nextstate) in transitions}

    def is_valid(self):
        """Return True if every state and symbol in every transition exists
        in the states and alphabet."""
        return all(state in self.states
                   and symbol in self.alphabet
                   and nextstate in self.states
                   for (state, symbol), nextstate in self.transitions.items())

    def is_complete(self):
        """Return true if the DFA is complete. Assumes the DFA is valid."""
        return all((state, symbol) in self.transitions
                   for state in self.states
                   for symbol in self.alphabet)

    def process(self, state, sequence):
        """Take a state and sequence and returns the state reached (if any),
        None otherwise."""
        for symbol in sequence:
            nextstate = self.transitions.get((state, symbol), None)
            state = nextstate
            if state is None:
                break
        return state

    def recognizes(self, sequence):
        """Process a sequence from the initial state and returns True if a
        final state is reached."""
        return self.process(self.initial, sequence) in self.finals

    def complete(self):
        """Return a complete DFA."""
        new = copy.deepcopy(self)
        new.states.add("sink")
        for state in new.states:
            for symbol in new.alphabet:
                if (state, symbol) not in new.transitions:
                    new.transitions[(state, symbol)] = "sink"
        return new

    def complement(self):
        """Returns the complement of this DFA."""
        new = copy.deepcopy(self)
        new.finals = new.states - new.finals
        return new

    def _intersect_or_union(self, other, op):
        """Return the intersection or union of this DFA with another.
        Parameters `op` must be a string 'intersect' or 'union'."""
        if op == "intersect":
            boolfunc = operator.and_
        elif op == "union":
            boolfunc = operator.or_
        else:
            raise ValueError("`op` must be one of ('intersect', 'union').")

        states = set(product(self.states, other.states))
        alphabet = self.alphabet
        initial = (self.initial, other.initial)
        finals = {(s1, s2) for s1, s2 in states
                  if boolfunc(s1 in self.finals, s2 in other.finals)}
        transitions = [
            (state, symbol, nextstate)
            for state, symbol, nextstate in product(states, alphabet, states)
            if ((state[0], symbol), nextstate[0]) in self.transitions.items()
            and ((state[1], symbol), nextstate[1]) in other.transitions.items()]
        return FSA(states, alphabet, initial, finals, transitions)

    def intersect(self, other):
        """Return the intersection of this DFA with another. Assumes same
        alphabet for each."""
        if not self.alphabet == other.alphabet:
            raise ValueError("DFAs must have same alphabet in order to "
                             "calculate intersection.")
        return self._intersect_or_union(other, "intersect")

    def union(self, other):
        """Return the union of this DFA with another."""
        if not self.alphabet == other.alphabet:
            raise ValueError("DFAs must have same alphabet in order to "
                             "calculate union.")
        return self._intersect_or_union(other, "union")


if __name__ == "__main__":
    xs = {'a', 'b', 'c'}
    q0 = 0

    # even-a
    qs = {0, 1}
    fs = {0}
    ts = {(0, 'a', 1),
          (1, 'a', 0),
          (0, 'b', 0),
          (1, 'b', 1),
          (0, 'c', 0),
          (1, 'c', 1)}
    even_a = FSA(qs, xs, q0, fs, ts)

    # exact2bs
    qs2 = {0, 1, 2}
    fs2 = {2}
    ts2 = {(0, 'a', 0),
           (1, 'a', 1),
           (2, 'a', 2),
           (0, 'b', 1),
           (1, 'b', 2),
           (0, 'c', 0),
           (1, 'c', 1),
           (2, 'c', 2)}
    exact2bs = FSA(qs2, xs, q0, fs2, ts2)

    # invalid
    qs3 = {}
    invalid1 = FSA(qs3, xs, q0, fs, ts)
    xs4 = {'a', 'b'}
    invalid2 = FSA(qs, xs4, q0, fs, ts)

    totale2bs = exact2bs.complete()
    intersect = even_a.intersect(totale2bs)
    union = even_a.union(totale2bs)
    comp = even_a.complement()

    print("even_a is valid: {0}".format(even_a.is_valid()))
    print("even_a is complete: {0}".format(even_a.is_complete()))
    print("exact2bs is valid: {0}".format(exact2bs.is_valid()))
    print("exact2bs is complete: {0}".format(exact2bs.is_complete()))
    print("completing of exact2bs is complete: {0}".format(totale2bs.is_complete()))
    print("even_a with empty state set is valid: {0}".format(invalid1.is_valid()))
    print("even_a with empty alphabet is valid: {0}".format(invalid2.is_valid()))

    test_words = ['aba', 'abaa', 'bb', 'ccacc', 'bcccbaa', 'aabcbcbcbc',
                  'aaaabaaaabccccc', 'ababa']

    # from prettytable import PrettyTable
    # table = PrettyTable()
    # table.field_names = ["Sequence", "Even-a accepts?", "Exactly2bs?",
    #                      "Int?", "Union?", "Comp of even-a?"]
    # for w in test_words:
    #     a = even_a.recognizes(w)
    #     b = totale2bs.recognizes(w)
    #     c = intersect.recognizes(w)
    #     d = union.recognizes(w)
    #     e = comp.recognizes(w)
    #     table.add_row([w, a, b, c, d, e])
    # print(table)
