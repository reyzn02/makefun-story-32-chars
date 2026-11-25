#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters.

The program writes a single Wi-Fi network name, at most 32
characters, that hints at a whole story. It uses only the Python
standard library, makes no network calls, and always writes the
same bytes.
"""

import os

LINE = "Sorry_The_WiFi_Died_With_Grandma"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
