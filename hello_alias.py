import argparse

VERSION = "alias-0.1"


def main() -> None:
    parser = argparse.ArgumentParser(prog="hello_alias")
    parser.add_argument("--version", action="store_true")
    args = parser.parse_args()
    if args.version:
        print(VERSION)
    else:
        print("hello alias")


if __name__ == "__main__":
    main()
