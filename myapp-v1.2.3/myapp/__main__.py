"""
myapp
"""
import os
import sys

def main(argv: list[str] = sys.argv[1:]) -> int:
    keys = (
        k for k in os.environ
        if k.startswith("MYAPP")
    )
    print("MyApp Settings")
    for k in keys:
        print(f"{k}={os.environ[k]!r}")

if __name__ == "__main__":
    main()