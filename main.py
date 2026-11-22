"""make.fun entry: Sum up 22 November's world news in one image.

The simplest deterministic program: copy the image held in this
repository (entry.png) to /output/entry.png. No network, no randomness,
no timestamps -- both runs write the same bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.png")


def main() -> None:
    out_dir = os.path.dirname(DST)
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, DST)
    # make.fun collects /output as another user than the one this runs as,
    # so the copy should be readable by everyone, whatever the umask.
    # Never fail the run over it: the grader's /output may belong to
    # another user, and only the file this process just created is ours.
    try:
        os.chmod(DST, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
    sys.exit(0)
