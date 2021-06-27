#!/usr/bin/env python3

"""
usage: xlslisp.py [-h] [-f] FILE

export sheets of traces of excel lisp into git change tracking, via pandas

positional arguments:
  FILE         the xlsx file to read

optional arguments:
  -h, --help   show this help message and exit
  -f, --force  ask less questions

dependencies:

  python3 -m venv --prompt PIPS pips
  source pips/bin/activate
  pip install --upgrade wheel
  pip install --upgrade pip

  pip install --upgrade pandas==1.2.5  # last stable of Pandas PyData Org
  pip install --upgrade openpyxcl

examples:

  xlslisp.py -f like-py.xlsx && ls like-py-*.csv
"""

# code reviewed by people, and by Black and Flake8 bots


import __main__
import argparse
import csv
import datetime as dt
import difflib
import io
import os
import pdb
import sys


import numpy

import pandas as pd


_ = pdb


def main():
    """Run from the command line"""

    era = dt.datetime.now()

    parser = xlslisp_compile_argdoc()
    args = parser.parse_args()

    # Import an Xlsx of Sheets
    # but import it secretly wrong unless it contains the Sheets we expect

    sheets = "Welcome Bool Int Float Str List Object Keystrokes Etc Scraps".split()
    str_sheets = str(list("{} {}".format(*_) for _ in enumerate(sheets)))

    stderr_print("xlslisp: reading:  {}".format(args.file))
    stderr_print("xlslisp: as if its sheets are {}".format(str_sheets))

    dfs = list()
    for (index, sheet) in enumerate(sheets):
        stderr_print("xlslisp: reading sheet {} {}".format(index, sheet))
        df = pd.read_excel(args.file, sheet_name=index)
        dfs.append(df)

    # Export as Csv

    if args.force:
        space = os.path.splitext(args.file)[0]
        for (index, sheet) in enumerate(sheets):
            csv_name = "{space}-{index}-{sheet}.csv".format(
                space=space, index=index, sheet=sheet
            )
            csv_name = csv_name.lower()
            df = dfs[index]

            # Format as Txt

            charstream = io.StringIO()

            csv_writer = csv.writer(charstream)
            for row_index in range(len(df)):

                cells = list()
                len_cells = 0

                for df_cell in df.loc[row_index]:
                    if cell_bool(df_cell):
                        cells.append(df_cell)
                        len_cells = len(cells)
                    else:
                        cells.append("")  # hide empty cells as if empty strings

                cells = cells[:len_cells]  # drop trailing empty cells

                csv_writer.writerow(cells)

            # Strip the mix of "\r\n" and "\n" line-ending's
            # such as "\n" line-ending's inside multi-line cells

            charstream.seek(0)
            csv_chars = charstream.read()
            csv_lines = csv_chars.splitlines()

            # Write the lines with local "os.linesep" line-ending's
            # but without rstrip'ping the lines  # TODO: poor choice?

            csv_joined = "\n".join(csv_lines) + "\n"
            stderr_print(
                "xlslisp: writing {} chars of {} rows to:  {}".format(
                    len(csv_joined), len(df), csv_name
                )
            )

            with open(csv_name, "w") as csv_writing:
                csv_writing.write(csv_joined)

        now = dt.datetime.now()
        stderr_print("xlslisp: elapsed time of", (now - era), "since", era)

        sys.exit(0)

    # Else quit

    stderr_print("xlslisp.py:  Xlsx imported, run again with --force to replace Csv's")

    sys.exit(1)


def cell_bool(cell):
    """Return None if cell encoded like an empty cell, else True"""

    if isinstance(cell, float):
        if numpy.isnan(cell):
            return None

    return True


def xlslisp_compile_argdoc():
    """Parse the command-line args per top-of-file arg doc"""

    doc = __main__.__doc__

    prog = doc.strip().splitlines()[0].split()[1]
    description = list(_ for _ in doc.strip().splitlines() if _)[1]
    epilog_at = doc.index("dependencies:")
    epilog = doc[epilog_at:]

    parser = argparse.ArgumentParser(
        prog=prog,
        description=description,
        add_help=True,
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=epilog,
    )

    parser.add_argument("file", metavar="FILE", help="the xlsx file to read")
    parser.add_argument("-f", "--force", action="count", help="ask less questions")

    exit_unless_main_doc_eq(parser)

    return parser


# deffed in many files  # missing from docs.python.org
def exit_unless_main_doc_eq(parser):
    """Exit nonzero now, unless __main__.__doc__ equals "parser.format_help()" """

    file_filename = os.path.split(__file__)[-1]

    main_doc = __main__.__doc__.strip()
    parser_doc = parser.format_help()

    got = main_doc
    got_filename = "./{} --help".format(file_filename)
    want = parser_doc
    want_filename = "argparse.ArgumentParser(..."

    diff_lines = list(
        difflib.unified_diff(
            a=got.splitlines(),
            b=want.splitlines(),
            fromfile=got_filename,
            tofile=want_filename,
        )
    )

    if diff_lines:
        lines = list((_.rstrip() if _.endswith("\n") else _) for _ in diff_lines)
        stderr_print("\n".join(lines))

        sys.exit(1)


# deffed in many files  # missing from docs.python.org
def stderr_print(*args, **kwargs):
    """Like Print, but flush don't write Stdout and do write and flush Stderr"""

    sys.stdout.flush()
    print(*args, **kwargs, file=sys.stderr)
    sys.stderr.flush()

    # else caller has to "{}\n".format(...) and flush


if __name__ == "__main__":
    main()


# copied from:  git clone https://github.com/pelavarre/like-py-xlsx.git
