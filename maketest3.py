import json, os
import subprocess, sys

def pdf(texts):
    objs = [None, "<< /Type /Catalog /Pages 2 0 R >>", None, "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"]
    kids = []
    for t in texts:
        body = "BT /F1 72 Tf 120 400 Td (%s) Tj ET" % t
        objs.append("<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 3 0 R >> >> /Contents %d 0 R >>" % (len(objs) + 1))
        kids.append("%d 0 R" % (len(objs) - 1))
        objs.append("<< /Length %d >>\nstream\n%s\nendstream" % (len(body), body))
    objs[2] = "<< /Type /Pages /Kids [%s] /Count %d >>" % (" ".join(kids), len(texts))
    out, offs = "%PDF-1.4\n", []
    for i in range(1, len(objs)):
        offs.append(len(out))
        out += "%d 0 obj\n%s\nendobj\n" % (i, objs[i])
    x = len(out)
    out += "xref\n0 %d\n0000000000 65535 f \n" % len(objs) + "".join("%010d 00000 n \n" % o for o in offs)
    out += "trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (len(objs), x)
    return out.encode("latin-1")

if sys.argv[1:] == ["pdf"]:
    import base64
    open("doc.pdf", "wb").write(pdf(["Page one", "Page two", "Page three"]))
    chart = subprocess.run(["convert", "-size", "240x160", "xc:white", "-fill", "orange", "-draw", "rectangle 30,40 90,150", "-draw", "rectangle 140,90 200,150", "png:-"], check=True, capture_output=True).stdout
    open("chart.ipynb", "w").write(json.dumps({"cells": [{"cell_type": "code", "execution_count": 1, "metadata": {}, "source": ["plot()"],
        "outputs": [{"output_type": "display_data", "metadata": {}, "data": {"image/png": base64.b64encode(chart).decode()}}]}], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}))
    print("made doc.pdf and chart.ipynb")
    sys.exit(0)


W = "the quick brown fox jumps over the lazy dog near a quiet river bank".split()
open("part.txt", "w").write("".join("part line %d: %s\n" % (n, " ".join(W[(n + i) % len(W)] for i in range(14))) for n in range(1, 1501)))
open("plain.txt", "w").write("original plain text\n")
open("old.txt", "wb").write(b"caf\xe9 au lait\n")
open("u16.txt", "wb").write(b"\xff\xfe" + "héllo utf16\n".encode("utf-16-le"))
open("target.txt", "w").write("target original\n")
os.makedirs("realdir", exist_ok=True)
open("realdir/keep.txt", "w").write("keeps the folder\n")
for name, to in (("link.txt", "target.txt"), ("linkdir", "realdir")):
    if os.path.lexists(name):
        os.remove(name)
    os.symlink(to, name)
open("nb.ipynb", "w").write(json.dumps({"cells": [{"cell_type": "code", "execution_count": 1, "metadata": {}, "source": ["print(1)"],
    "outputs": [{"output_type": "stream", "name": "stdout", "text": ["1\n"]}]}], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}))
print("made the test files")
