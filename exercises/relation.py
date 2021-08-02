"""
Class representing a mathematical relation.
"""

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
        return all((y, x) in self.mapping for (x, y) in self.mapping)

    def is_irreflexive(self):
        return not self.is_reflexive()

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


if __name__ == "__main__":
    r1 = Relation(set("abcd"), [("a","a"), ("b","b"), ("c","c")])
    r2 = Relation(set("abcd"), [("a","a"), ("b","b"), ("c","d")])
    r3 = Relation(set("abcd"), [("a","b"), ("b","c"), ("c","d"),
                                ("a","c"), ("b","d"), ("a","d")])
    r4 = Relation(set("abcd"), [("a","b"), ("b","a"), ("c","d"), ("d","c")])
    r5 = Relation(set("abcd"), [("a","b"), ("b","a"), ("c","d"), ("d","d")])

    for i, r in enumerate((r1, r2, r3, r4, r5)):
        print(i + 1)
        print(r)
        print("reflexive", r.is_reflexive())
        print("irreflexive", r.is_irreflexive())
        print("symmetric", r.is_symmetric())
        print("antisymmetric", r.is_antisymmetric())
        print("asymmetric", r.is_asymmetric())
        print()

