import pathlib

GID = "G-FVZHH3RMRT"
snippet = f'''<script async src="https://www.googletagmanager.com/gtag/js?id={GID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GID}');
</script>
'''
for p in sorted(pathlib.Path(".").glob("*.html")) + sorted(pathlib.Path("articles").glob("*.html")):
    s = p.read_text(encoding="utf-8")
    if GID in s:
        print("skip", p)
        continue
    s = s.replace("</head>", snippet + "</head>")
    p.write_text(s, encoding="utf-8")
    print("updated", p)
