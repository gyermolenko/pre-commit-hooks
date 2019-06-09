import argparse
import ast


class NamedExprVisitor(ast.NodeVisitor):
    def __init__(self):
        self.lineno = None

    def visit_NamedExpr(self, node):
        self.lineno = node.lineno


def check(filename):
    with open(filename) as f:
        contents = f.read()

    try:
        tree = ast.parse(contents)
    except SyntaxError:
        print('SyntaxError, continue')
        return

    visitor = NamedExprVisitor()
    visitor.visit(tree)
    return visitor.lineno


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args()

    for filename in args.filenames:
        lineno = check(filename)
        if lineno:
            print(f"{filename}:{lineno}")
            return 1

    return 0


if __name__ == '__main__':
    exit(main())
