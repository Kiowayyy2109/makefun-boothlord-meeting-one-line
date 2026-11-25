#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line — one line about meetings."""
import os

LINE = "This meeting could have been an email. The email could have been a text. The text could have been silence. We chose violence."
assert len(LINE) == 125, "entry must be exactly 125 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
