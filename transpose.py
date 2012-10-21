#! /usr/bin/env python

import sys


def main():
    space = {}

    maxcol = 0

    for (row, line) in enumerate(sys.stdin):
        for (col, inchar) in enumerate(line.rstrip()):
            space[(col,row)] = inchar
        maxcol = max(maxcol, col)
    maxrow = row
    #sys.stderr.write('DEBUG: maxcol %r; maxrow %r\n' % (maxcol, maxrow))

    for col in range(maxcol+1):
        for row in range(maxrow+1):
            inchar = space.get( (col, row), ' ' )
            outchar = CHAR_TRANSLATIONS.get(inchar, inchar)
            #sys.stderr.write('DEBUG: <%r,%r> %r -> <%r,%r> %r\n' % (col,row,inchar,row,col,outchar))
            sys.stdout.write(outchar)
        sys.stdout.write('\n')


CHAR_TRANSLATIONS = {
    '>': 'v',
    '<': '^',
    'v': '>',
    '^': '<',
    '|': '_',
    '_': '|',
    }




if __name__ == '__main__':
    main()
