import argparse

def main(argv=None):
    parser=argparse.ArgumentParser(prog="demo-engineering")
    parser.add_argument("name", nargs="?", default="world")
    args=parser.parse_args(argv)
    print(f"hello {args.name}")
    return 0
