"""Notification of favorite feature

>>> os.environ['MY_FAVORITE_FEATURE'] = "echo"
>>> main()
What about echo?
"""
import os
def main() -> None:
    print(f"What about {os.environ['MY_FAVORITE_FEATURE']}?")
if __name__ == "__main__":
    main()

