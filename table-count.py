import sys
import argparse
import logging


def main() -> int:
    parser = argparse.ArgumentParser(
                    prog='HTML Table Counter',
                    description='Counts the number of tables, as well as the rows and columns, in the HTM/HTML file',
                    epilog='Version 0.0.1')
    parser.add_argument("filename", help="name or path to the htm/html file to check")
    args = parser.parse_args()

    filename = args.filename
    if not filename:
        logging.error('Missing filename, quitting')
        return 1

    count(filename)

    return 0


def count(filename) -> None:
    tbl_count = 0
    first_col = False
    rows, columns = 0, 0
    srcfile = open(filename)
    results = open('results.csv', 'w')
    results.write('Table_Title, Table_num, Num_columns, Num_Rows,\n')
    for line in srcfile:
        if '<table' in line:
            tbl_count += 1
            first_col = True
        if '<tr' in line:
            columns += 1
        if first_col and '<td' in line:
            rows += 1
        if first_col and '</tr>' in line:
            first_col = False
        if '<!--' in line:
            results.write(line.split("\n")[0])
        if '</table>' in line:
            results.write(f",{tbl_count}, {columns}, {rows},\n")
            rows = 0
            columns = 0

    srcfile.close()
    results.close()


if __name__ == '__main__':
    sys.exit(main())
