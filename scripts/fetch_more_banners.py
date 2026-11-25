import urllib.request, pathlib
from PIL import Image

OUT = pathlib.Path("assets")
URLS = {
 "flets": [
  "https://www20.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011049000&mc=1",
  "https://www20.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011034000&mc=1",
  "https://www29.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011030000&mc=1",
  "https://www25.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011035000&mc=1",
  "https://www24.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011047000&mc=1",
  "https://www25.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011033000&mc=1",
  "https://www22.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011038000&mc=1",
  "https://www20.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011073000&mc=1",
  "https://www26.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011028000&mc=1",
  "https://www28.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011002000&mc=1",
  "https://www28.a8.net/svt/bgt?aid=261125343026&wid=003&eno=01&mid=s00000007633011003000&mc=1",
 ],
 "softbank2": [
  "https://www25.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043004000&mc=1",
  "https://www22.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043011000&mc=1",
  "https://www28.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043009000&mc=1",
  "https://www20.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043033000&mc=1",
  "https://www22.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043005000&mc=1",
  "https://www21.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043006000&mc=1",
  "https://www24.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043007000&mc=1",
  "https://www23.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043008000&mc=1",
  "https://www24.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043012000&mc=1",
  "https://www22.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043013000&mc=1",
  "https://www24.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043024000&mc=1",
  "https://www28.a8.net/svt/bgt?aid=261125343004&wid=003&eno=01&mid=s00000000018043025000&mc=1",
 ],
}
for name, urls in URLS.items():
    best = None
    for i, u in enumerate(urls):
        try:
            data = urllib.request.urlopen(u, timeout=15).read()
            p = OUT / f"tmp2-{name}-{i}.jpg"
            p.write_bytes(data)
            im = Image.open(p).copy()
            ratio = im.width / im.height
            if 0.9 <= ratio <= 2.2 and (best is None or im.width * im.height > best[1].width * best[1].height):
                best = (p, im)
        except Exception as e:
            print("fail", name, i, e)
    if best:
        out = OUT / f"provider-{name}.jpg"
        best[1].convert("RGB").save(out, "JPEG", quality=88, optimize=True)
        print(name, best[1].size, out.stat().st_size)
