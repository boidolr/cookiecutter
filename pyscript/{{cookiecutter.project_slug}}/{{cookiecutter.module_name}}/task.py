import argparse
import sys
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="{{ cookiecutter.console_entry }}",
        description="{{ cookiecutter.short_description }}",
    )
    args = parser.parse_args(argv)

    print(f"Received {args} to process")
    return 0


if __name__ == "__main__":
    sys.exit(main())
