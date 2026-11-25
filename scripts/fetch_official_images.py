import urllib.request, pathlib
from PIL import Image

OUT = pathlib.Path("assets")
URLS = {
    "nuro-kv": "https://www.nuro.jp/assets/next/img/kv_2980yen-pc.jpg?v=086a9a3a75",
    "nuro-ogp": "https://www.nuro.jp/assets/next/shared/img/ogp.jpg",
    "au-bnr06": "https://www.au.com/content/dam/au-com/internet/images/in_internet_bnr06_f4c6dc27ce140f7f.jpg",
    "au-bnr07": "https://www.au.com/content/dam/au-com/internet/images/in_internet_bnr07_4805bbfcc67dcfbe.jpg",
}
for name, url in URLS.items():
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=20).read()
        p = OUT / f"official-{name}.jpg"
        p.write_bytes(data)
        print(name, Image.open(p).size, len(data))
    except Exception as e:
        print("FAIL", name, e)
