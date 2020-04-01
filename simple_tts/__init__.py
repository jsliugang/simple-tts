# Copyright 2019, Rasmus Sorensen <rasmusscholer@gmail.com>
"""


"""

import sys

if sys.platform == "win32":
    from .tts_win import *
else:
    raise RuntimeError(
        "simple-tts currently only runs on Windows. We welcome contributions enabling TTS support on macOS and Linux. "
        "Please see README.md for alternative python packages that do support macOS and Linux."
    )
