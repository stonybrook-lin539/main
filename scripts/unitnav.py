#!/usr/bin/env python3
"""
Code to automatically determine structure of course notes.
Allows lookup of chapter and section numbers,
determination of next/previous section, etc.
"""

from collections import namedtuple
from pathlib import Path

Unit = namedtuple("Unit", ["part", "chnum", "ch", "secnum", "sec"])
SRCDIR = Path("source/main")


class UnitDB:
    def __init__(self, path):
        self.db = {}
        for p in path.glob("**/*.md"):
            part, ch, sec = p.parts[1:]
            sec = sec.removesuffix(".md")
            try:
                chnum, chname = ch.split("_", 1)
            except ValueError:
                raise ValueError(f"Missing chapter num: {ch}")
            try:
                secnum, secname = sec.split("_", 1)
            except ValueError:
                raise ValueError(f"Missing section num: {sec}")
            chnum = int(chnum)
            secnum = int(secnum)
            uid = chname + '/' + secname
            self.db[uid] = (Unit(part, chnum, ch, secnum, sec))

    def to_tsv(self):
        lines = []
        for uid, e in self.db.items():
            lines.append('\t'.join([uid, e.part, str(e.chnum), e.ch,
                                    str(e.secnum), e.sec]))
        return('\n'.join(lines))

    def next_unit(self, uid, reverse=False):
        entry = self.db.get(uid)
        currunit = (entry.chnum, entry.secnum, uid)
        units = sorted(((e.chnum, e.secnum, uid) for uid, e in self.db.items()),
                       reverse=reverse)
        return next(u for u in units if u > currunit)[2]

    def prev_unit(self, uid):
        return self.next_unit(uid, reverse=True)


if __name__ == "__main__":
    db = UnitDB(SRCDIR)
    print(db.to_tsv())
    # pprint(db)
    unit = "universals/paradigms"
    print(unit)
    print(db.next_unit(unit))
    print(db.prev_unit(unit))
