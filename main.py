# SPDX-License-Identifier: MIT
"""Write the one-line cat joke to /output/entry.txt."""
import os

JOKE = "My cat never begs; she stands by her empty bowl and lets the silence do the negotiating."


def main():
    # The grader provides /output; fall back to a local folder when run elsewhere.
    out_dir = "/output" if os.path.isdir("/output") or os.access("/", os.W_OK) else "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    assert 1 <= len(JOKE) <= 200 and "\n" not in JOKE and JOKE.strip()
    return path


if __name__ == "__main__":
    main()
