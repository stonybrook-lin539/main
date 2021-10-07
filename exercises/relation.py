"""
Class representing a mathematical relation.
"""

from itertools import combinations

import pydot


class Relation:

    def __init__(self, domain, mapping):
        """
        domain - set of elements
        mapping - set of pairs of elements in the domain
        """
        if (not all(x in domain and y in domain for x, y in mapping)):
            raise ValueError("Mapping contains element not in domain")
        self.domain = domain
        self.mapping = mapping

    def __str__(self):
        return ("<Relation>"
                f"\nDomain: {self.domain}"
                f"\nMapping: {self.mapping}")

    def to_pydot(self):
        g = pydot.Dot("relation", graph_type="digraph", rankdir="LR")
        g.set_node_defaults(shape="circle")
        for node in self.domain:
            g.add_node(pydot.Node(node))
        for edge in self.mapping:
            g.add_edge(pydot.Edge(*edge))
        return g

    def is_reflexive(self):
        return all((x, x) in self.mapping for x in self.domain)

    def is_irreflexive(self):
        return not any((x, x) in self.mapping for x in self.domain)

    def is_transitive(self):
        return all((a, d) in self.mapping
                   for (a, b) in self.mapping
                   for (c, d) in self.mapping
                   if b == c)

    def is_symmetric(self):
        return all((y, x) in self.mapping for (x, y) in self.mapping)

    def is_antisymmetric(self):
        return not any((y, x) in self.mapping for (x, y) in self.mapping
                       if x != y)

    def is_asymmetric(self):
        return not any((y, x) in self.mapping for (x, y) in self.mapping)

    def make_reflexive(self):
        """Add elements to mapping to make the relation reflexive."""
        self.add_reflexive_pairs()
        assert self.is_reflexive()

    def make_irreflexive(self):
        """
        Remove elements from mapping to make the relation irreflexive.
        """
        self.remove_reflexive_pairs()
        assert self.is_irreflexive()

    def make_transitive(self):
        """Add elements to mapping to make the relation transitive."""
        for (a, b) in self.mapping:
            for (c, d) in self.mapping:
                if b == c and not (a, d) in self.mapping:
                    self.mapping.append((a, d))
        assert self.is_transitive()

    def make_symmetric(self):
        """Add elements to mapping to make the relation symmetric."""
        self.add_symmetric_pairs()
        assert self.is_symmetric()

    def make_antisymmetric(self):
        """
        Remove elements from mapping to make the relation antisymmetric. When
        there is a pair of elements (x, y) and (y, x), remove the element that
        is ordered last by sorting.
        """
        self.remove_symmetric_pairs()
        assert self.is_antisymmetric()

    def make_asymmetric(self):
        """
        Remove elements from mapping to make the relation asymmetric. When
        there is a pair of elements (x, y) and (y, x), remove the element that
        is ordered last by sorting.
        """
        self.remove_reflexive_pairs()
        self.remove_symmetric_pairs()
        assert self.is_asymmetric()

    def add_reflexive_pairs(self):
        """Add (x, x) to mapping for every element x in the domain."""
        for x in self.domain:
            if not (x, x) in self.mapping:
                self.mapping.append((x, x))

    def remove_reflexive_pairs(self):
        """
        Remove all elements (x, x) in the mapping. Iterate over a copy, since
        we are removing elements while iterating.
        """
        for (x, y) in self.mapping[:]:
            if x == y:
                self.mapping.remove((x, x))

    def add_symmetric_pairs(self):
        """Add (y, x) to for every (x, y) in the mapping, if not present."""
        for (x, y) in self.mapping:
            if not (y, x) in self.mapping:
                self.mapping.append((y, x))

    def remove_symmetric_pairs(self):
        """
        When there is a pair of elements (x, y) and (y, x) in the mapping,
        remove the element that is ordered last by sorting.

        The simplest way to do this is to check all combinations of elements,
        decide which to remove, and then do removal in a separate step.
        Iterating over a copy doesn't work for this, and creating a new list
        and replacing the old one can cause strange bugs.
        """
        toremove = []
        for (a, b), (c, d) in combinations(self.mapping, 2):
            if a == d and b == c:
                toremove.append((c, d))
        for (x, y) in toremove:
            self.mapping.remove((x, y))


if __name__ == "__main__":
    r1 = Relation(set("abcd"), [("a","a"), ("b","b"), ("c","c"), ("d", "d")])
    r2 = Relation(set("abcd"), [("a","a"), ("b","b"), ("c","d")])
    r3 = Relation(set("abcd"), [("a","b"), ("b","c"), ("c","d"),
                                ("a","c"), ("b","d"), ("a","d")])
    r4 = Relation(set("abcd"), [("a","b"), ("b","a"), ("c","d"), ("d","c")])
    r5 = Relation(set("abcd"), [("a","b"), ("b","a"), ("c","d"), ("d","d")])

    # for i, r in enumerate((r1, r2, r3, r4, r5)):
    #     print(i + 1)
    #     print(r)
    #     print("reflexive", r.is_reflexive())
    #     print("irreflexive", r.is_irreflexive())
    #     print("symmetric", r.is_symmetric())
    #     print("antisymmetric", r.is_antisymmetric())
    #     print("asymmetric", r.is_asymmetric())
    #     print()

    # print(r5)

    # r5.make_reflexive()
    # print(r5)

    # r5.make_irreflexive()
    # print(r5)

    # r5.make_transitive()
    # print(r5)

    # r5.make_symmetric()
    # print(r5)

    # r5.make_antisymmetric()
    # print(r5)

    # r5.make_asymmetric()
    # print(r5)
