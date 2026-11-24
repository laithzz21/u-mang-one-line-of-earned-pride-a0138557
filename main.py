#!/usr/bin/env python3
"""Entry for make.fun bounty: one line of earned pride.

Prints the single-line entry to stdout and also writes it to the output
directory (``/output/entry.txt`` by default, or ``$MAKEFUN_OUTPUT`` when
set), verifying the written file by reading it back.

Python 3.13, stdlib only, deterministic: no network, clock, or randomness.
"""

import os
import sys

ENTRY = (
    "My mother studied for her nursing exams by flashlight after her "
    "shifts for six years, and last month she walked into the clinic, "
    "read the chart herself, and signed it — 'R. Haddad, RN' — with no "
    "one standing behind her."
)


def validate(text: str) -> None:
    """The entry must be a single line of 1-240 characters."""
    if not 1 <= len(text) <= 240:
        raise ValueError(f"entry must be 1-240 characters, got {len(text)}")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if any(ch in text for ch in ("\n", "\r", "\x0b", "\x0c", "\u2028", "\u2029")):
        raise ValueError("entry must be a single line")


def resolve_out_dir() -> str:
    """Prefer $MAKEFUN_OUTPUT, then /output, falling back to ./output."""
    requested = os.environ.get("MAKEFUN_OUTPUT") or "/output"
    try:
        os.makedirs(requested, exist_ok=True)
        probe = os.path.join(requested, ".write_probe")
        with open(probe, "w", encoding="utf-8") as f:
            f.write("ok")
        os.remove(probe)
        return requested
    except OSError:
        fallback = os.path.join(os.getcwd(), "output")
        os.makedirs(fallback, exist_ok=True)
        return fallback


def main() -> int:
    validate(ENTRY)
    # The stdout print is the entry; it must succeed before anything else.
    print(ENTRY, flush=True)
    try:
        out_dir = resolve_out_dir()
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        # Verify the written file by reading it back.
        with open(path, "r", encoding="utf-8") as f:
            written = f.read()
        if written != ENTRY:
            raise RuntimeError("verification failed: written entry does not match")
    except (OSError, RuntimeError) as exc:
        # File output is a convenience copy only; the printed entry is
        # already out, so a failed write must not fail the run.
        print(f"warning: could not write entry.txt: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
