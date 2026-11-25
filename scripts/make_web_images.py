from PIL import Image
from pathlib import Path

ASSETS = Path("assets")
ASSETS.mkdir(exist_ok=True)

jobs = [
    ("sns/assets/osechi-real-test.jpg", "osechi-hero.jpg", (1200, 800)),
    ("sns/assets/kani-real-test.jpg", "kani-hero.jpg", (1200, 800)),
    ("sns/assets/osechi-real-test.jpg", "osechi-thumb.jpg", (600, 600)),
    ("sns/assets/kani-real-test.jpg", "kani-thumb.jpg", (600, 600)),
]

for src, out, size in jobs:
    im = Image.open(src).convert("RGB")
    w, h = im.size
    tw, th = size
    # center crop to target aspect
    target_ratio = tw / th
    if w / h > target_ratio:
        nw = int(h * target_ratio)
        left = (w - nw) // 2
        im = im.crop((left, 0, left + nw, h))
    else:
        nh = int(w / target_ratio)
        top = (h - nh) // 2
        im = im.crop((0, top, w, top + nh))
    im = im.resize(size, Image.LANCZOS)
    p = ASSETS / out
    im.save(p, "JPEG", quality=82, optimize=True)
    print(out, p.stat().st_size)
