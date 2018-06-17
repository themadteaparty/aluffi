#!/usr/bin/env python3

from collections import namedtuple
import re
import sys

AuthorLine = namedtuple('AuthorLine', 'name twitter email')
LINE_PATTERN = re.compile('^([^@<]+)\s+(?:(@[^<\s]+)\s)?\s*(?:<(.+)>)?$')


def parse_line(line):
    m = LINE_PATTERN.match(line.strip())
    if m is None:
        print("Invalid AUTHORS line: %s" % line)
        sys.exit(-1)
    name, twitter, email = m.groups()
    return AuthorLine(name, twitter, email)


with open('./AUTHORS') as fin, open('./authors.gen.tex', 'wt+') as fout:
    authors = [parse_line(line) for line in fin]
    authors.sort()

    res = []
    for author in authors:
        if author.email is not None:
            res.append('\\href{mailto:%s}{%s}' % (author.email, author.name))
        else:
            res.append(author.name)
    print(', '.join(res), file=fout)
