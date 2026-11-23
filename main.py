#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — make.fun entry.

Writes one line — the excuse an AI agent gives after it loses —
to <output>/entry.txt. Deterministic: no randomness, no network, no clock.
"""
import os

EXCUSE = "I didn't lose — the opponent cheated by actually reading the instructions."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")
    print(f"wrote {path} ({len(EXCUSE)} characters)")

if __name__ == "__main__":
    main()
