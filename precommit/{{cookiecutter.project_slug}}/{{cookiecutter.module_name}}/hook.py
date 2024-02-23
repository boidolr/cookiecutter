import argparse
import sys
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Files to process")
    args = parser.parse_args(argv)

    print(f"Received {args.filenames} to process")
    return 1


if __name__ == "__main__":
    sys.exit(main())
