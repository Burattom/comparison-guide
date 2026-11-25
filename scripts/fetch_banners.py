import urllib.request, pathlib
from PIL import Image

OUT = pathlib.Path("assets")
OUT.mkdir(exist_ok=True)

URLS = {
    "docomo": [
        "https://www28.a8.net/svt/bgt?aid=261125340216&wid=003&eno=01&mid=s00000000018031044000&mc=1",
        "https://www24.a8.net/svt/bgt?aid=261125340216&wid=003&eno=01&mid=s00000000018031023000&mc=1",
        "https://www24.a8.net/svt/bgt?aid=261125340216&wid=003&eno=01&mid=s00000000018031075000&mc=1",
        "https://www27.a8.net/svt/bgt?aid=261125340216&wid=003&eno=01&mid=s00000000018031033000&mc=1",
        "https://www24.a8.net/svt/bgt?aid=261125340216&wid=003&eno=01&mid=s00000000018031086000&mc=1",
        "https://www26.a8.net/svt/bgt?aid=261125340216&wid=003&eno=01&mid=s00000000018031015000&mc=1",
    ],
    "gmo": [
        "https://www23.a8.net/svt/bgt?aid=261125340184&wid=003&eno=01&mid=s00000000018040010000&mc=1",
        "https://www28.a8.net/svt/bgt?aid=261125340184&wid=003&eno=01&mid=s00000000018040038000&mc=1",
        "https://www27.a8.net/svt/bgt?aid=261125340184&wid=003&eno=01&mid=s00000000018040023000&mc=1",
        "https://www21.a8.net/svt/bgt?aid=261125340184&wid=003&eno=01&mid=s00000000018040016000&mc=1",
        "https://www20.a8.net/svt/bgt?aid=261125340184&wid=003&eno=01&mid=s00000000018040032000&mc=1",
        "https://www23.a8.net/svt/bgt?aid=261125340184&wid=003&eno=01&mid=s00000000018040008000&mc=1",
    ],
    "softbank": [
        "https://www21.a8.net/svt/bgt?aid=261125343017&wid=003&eno=01&mid=s00000014546008008000&mc=1",
        "https://www23.a8.net/svt/bgt?aid=261125343017&wid=003&eno=01&mid=s00000014546008006000&mc=1",
        "https://www22.a8.net/svt/bgt?aid=261125343017&wid=003&eno=01&mid=s00000014546008004000&mc=1",
        "https://www27.a8.net/svt/bgt?aid=261125343017&wid=003&eno=01&mid=s00000014546008005000&mc=1",
        "https://www29.a8.net/svt/bgt?aid=261125343017&wid=003&eno=01&mid=s00000014546008007000&mc=1",
        "https://www29.a8.net/svt/bgt?aid=261125343017&wid=003&eno=01&mid=s00000014546008009000&mc=1",
    ],
    "softbank2": [
        "https://www29.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043010000&mc=1",
        "https://www24.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043028000&mc=1",
        "https://www25.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043004000&mc=1",
        "https://www22.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043011000&mc=1",
        "https://www28.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043009000&mc=1",
        "https://www20.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043033000&mc=1",
    ],
    "flets": [
        "https://www23.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011027000&mc=1",
        "https://www23.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011006000&mc=1",
        "https://www20.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011004000&mc=1",
        "https://www20.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011049000&mc=1",
        "https://www20.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011034000&mc=1",
        "https://www29.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011030000&mc=1",
    ],
}

for name, urls in URLS.items():
    best = None
    for i, u in enumerate(urls):
        try:
            data = urllib.request.urlopen(u, timeout=15).read()
            p = OUT / f"tmp-{name}-{i}.jpg"
            p.write_bytes(data)
            im = Image.open(p)
            if best is None or im.width * im.height > best[1].width * best[1].height:
                best = (p, im.copy())
        except Exception as e:
            print("fail", name, i, e)
    if best:
        out = OUT / f"provider-{name}.jpg"
        best[1].convert("RGB").save(out, "JPEG", quality=88, optimize=True)
        print(name, best[1].size, out.stat().st_size)
