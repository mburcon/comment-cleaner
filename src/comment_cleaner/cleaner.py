import argparse
import sys


def clean(input: str) -> str:
    cleaned = []
    for line in input.splitlines():
        if not line.lstrip().startswith("#"):
            cleaned.append(line)
    return "\n".join(cleaned)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="File to clean")
    args = parser.parse_args()
    try:
        with open(args.file, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File {args.file} not found")
        sys.exit(1)

    cleaned = clean(content)

    with open(args.file, "w+") as f:
        f.writelines(cleaned)


if __name__ == "__main__":
    main()