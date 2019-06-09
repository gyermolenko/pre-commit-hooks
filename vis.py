import ast
import sys
import argparse

class WalrusLister(ast.NodeVisitor):
    def visit_NamedExpr(self, node):
        print("111111111111")
        # exit(1)
        
        # return 1
        # print(node.lineno)
        # self.generic_visit(node)



def check(filename):
    contents = open(filename).read()
    try:
        tree = ast.parse(contents)
    except SyntaxError:
        return
        
    WalrusLister().visit(tree)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args()

    # ret = 0
    for filename in args.filenames:
        check(filename)
        # ret |= fix_file(filename, args)
    # return ret


if __name__ == '__main__':
    exit(main())
