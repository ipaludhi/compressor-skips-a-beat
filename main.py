"""Compressor skips a beat — one-line vending machine pickup line entry.

Writes one fixed line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness, no input. Deterministic: every run writes
byte-identical output.

The line: "I hum all day for strangers, but you made my compressor skip a beat."

Why this line: it is unmistakably the machine speaking, in vocabulary no bar
pickup line could use — the hum it makes all day, and its compressor. The
punch is a heart pun built from machine parts ("skip a beat") and arrives in
the last three words. At 68 characters it reads in one breath, and it is warm
and flattering, never creepy: the machine is charmed, not watching.
"""

import os
from pathlib import Path

TEXT = "I hum all day for strangers, but you made my compressor skip a beat."


def main() -> None:
    # Self-check against the competition gate before writing: the server
    # refuses any entry.txt outside 1-200 characters or blank, so fail
    # loudly here instead of silently shipping an invalid entry.
    if not 1 <= len(TEXT) <= 200 or not TEXT.strip():
        raise SystemExit("entry.txt must be 1-200 non-blank characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
