import sys
import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
                    prog='HTML Table Counter',
                    description='Counts the number of tables, as well as the rows and columns, in the HTM/HTML file',
                    epilog='Version 0.0.1')
    parser.add_argument("filename", help="name or path to the htm/html file to check")
    args = parser.parse_args()

    filename = args.filename
    return 0


if __name__ == '__main__':
    sys.exit(main())
