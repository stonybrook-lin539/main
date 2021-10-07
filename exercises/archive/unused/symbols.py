
class Symbol:
    def __init__(self, name, symbol, shortname=None, altsym=None):
        self.name = name
        self.symbol = symbol
        self.shortname = shortname
        self.altsym = altsym

    def __str__(self):
        return f"<Symbol name='{self.name}' symbol='{self.symbol}'>"


SYMBOLS = [
    Symbol("set union", "∪", shortname="union"),
    Symbol("set intersection", "∩", shortname="intersection"),
    Symbol("set difference", "\\", shortname="difference"),
    Symbol("element of", '∈'),
    Symbol("not element of", '∉'),
    Symbol("subset", '⊆'),
    Symbol("strict subset", '⊂', altsym='⊊'),
    Symbol("superset", '⊇'),
    Symbol("strict superset", '⊃', altsym='⊋'),
    Symbol("string concatenation", '·', shortname="string concat"),
    Symbol("substring", '⊑'),
    Symbol("strict substring", '⊏', altsym='⋤'),
    Symbol("superstring", '⊒'),
    Symbol("strict superstring", '⊐', altsym='⋥'),
    Symbol("logical and", '∧', shortname="and"),
    Symbol("logical or", '∨', shortname="or"),
    Symbol("logical not", '¬', shortname="not"),
    Symbol("logical conditional", '→', shortname="conditional"),
    Symbol("logical biconditional", '↔', shortname="biconditional"),
    Symbol("logical xor", '⊗', shortname="xor"),
    Symbol("meet", '∧'),
    Symbol("join", '∨')
]

SYMBOL_TABLE = {}
for s in SYMBOLS:
    key = s.shortname if s.shortname is not None else s.name
    SYMBOL_TABLE[key] = s.symbol

if __name__ == "__main__":
    from pprint import pprint
    pprint([str(s) for s in SYMBOLS])
    # pprint(SYMBOL_TABLE)
