"""
Class representing a mathematical relation.
"""


class Relation:

    def __init__(self, domain, mapping):
        """
        domain - set of elements
        mapping - dictionary from elements to lists/tuples of elements
        """
        if (not all(e in domain for e in mapping)
                or not all(e in domain for rhs in mapping.values() for e in rhs)):
            raise ValueError("Mapping contains element not in domain")
        self.domain = domain
        self.mapping = mapping

    def __str__(self):
        return ("<Relation>"
                f"\nDomain: {self.domain}"
                f"\nMapping: {self.mapping}")

    def is_reflexive(self):
        return all(lhs in rhs for lhs, rhs in self.mapping.items())

    def is_irreflexive(self):
        return not self.is_reflexive()

    def is_transitive(self):
        return all(z in self.mapping[x]
                   for x in self.mapping
                   for y in self.mapping[x]
                   for z in self.mapping[y])

    def is_symmetric(self):
        return all(x in self.mapping[y]
                   for x in self.mapping
                   for y in self.mapping[x])

    def is_antisymmetric(self):
        pass

    def is_asymmetric(self):
        pass


if __name__ == "__main__":
    r1 = Relation(set("abcd"), {"a":["a"], "b":["b"], "c":["c"]})
    r2 = Relation(set("abcd"), {"a":["a"], "b":["b"], "c":["d"]})
    r3 = Relation(set("abcd"), {"a":["b"], "b":["a"], "c":["d"], "d":["c"]})
    r4 = Relation(set("abcd"), {"a":["b"], "b":["a"], "c":["d"], "d":["d"]})
    r5 = Relation(set("abcd"), {"a":"bcd", "b":"cd", "c":"d", "d":"d"})

    print(r1)
    print("reflexive", r1.is_reflexive())
    print(r2)
    print("reflexive", r2.is_reflexive())
    print(r3)
    print("transitive", r3.is_symmetric())
    print(r4)
    print("transitive", r4.is_symmetric())
    print(r5)
    print("transitive", r5.is_transitive())

