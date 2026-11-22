"""news-image-20261122 entry: copy the pre-rendered front page to /output/entry.png.

Standard library only. Deterministic: a byte-for-byte copy, so two runs
write identical bytes. The image itself (entry.png, 1024x1024, rendered
with PIL locally) is the front page for Sunday 22 November 2026: COP31
deadlock in Antalya leads, with Iran/Bahrain, the Sinaloa cartel capture,
the Shenzhen trilateral, the US stocks correction, the Peru quake, the
Cikande factory fire, Ukraine/Poland, the Rohingya ruling and GTA 6.

Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output
(mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py).
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(OUT, "entry.png"))
