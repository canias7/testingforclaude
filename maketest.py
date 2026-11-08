import base64, json, os, struct, subprocess, sys, zipfile

W = "the quick brown fox jumps over the lazy dog near a quiet river bank".split()
def words(n, k=14):
    return " ".join(W[(n + i) % len(W)] for i in range(k))
def put(path, data):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data if isinstance(data, bytes) else data.encode())

if sys.argv[1:] == ["scratch"]:
    os.makedirs("/tmp/coder-scratch", exist_ok=True)
    if not os.path.exists("/tmp/coder-scratch/pipe1"):
        os.mkfifo("/tmp/coder-scratch/pipe1")
    w, h = 8000, 6000
    row = (w * 3 + 3) & ~3
    size = 54 + row * h
    with open("/tmp/coder-scratch/huge.bmp", "wb") as f:
        f.write(b"BM" + struct.pack("<IHHI", size, 0, 0, 54) + struct.pack("<IiiHHIIiiII", 40, w, h, 1, 24, 0, row * h, 2835, 2835, 0, 0))
        f.truncate(size)
    print("made /tmp/coder-scratch/pipe1 and /tmp/coder-scratch/huge.bmp (%d MB)" % (size // 1000000))
    sys.exit(0)

# Text files
lines, n = [], 0
while sum(len(x) + 1 for x in lines) < 300000:
    n += 1
    lines.append("big line %d: %s" % (n, words(n)))
put("big.txt", "\n".join(lines) + "\n")
lines, n = [], 0
while sum(len(x) + 1 for x in lines) < 130000:
    n += 1
    lines.append("wide line %d: %s" % (n, words(n)))
put("wide.txt", "\n".join(lines) + "\n")
long2, k = [], 0
while len(" ".join(long2)) < 5000:
    k += 1
    long2.append("w%d" % k)
put("longline.txt", "first line\n" + " ".join(long2) + "\nthird line\n")
put("utf16.txt", b"\xff\xfe" + "héllo wörld, a UTF-16 file\nsecond line: ünïcödé ✓\n".encode("utf-16-le"))
put("notes.txt", "apple\nbanana\ncherry\n")
for i in range(1, 6):
    rows, m = [], 0
    while sum(len(x) + 1 for x in rows) < 95000:
        m += 1
        rows.append("part %d line %d: %s" % (i, m, words(m * i)))
    rows.append("part %d ends here" % i)
    put("part%d.txt" % i, "\n".join(rows) + "\n")

# Files for the @ list
put("src/cart.js", "export const cart = [];\n")
put("docs/cart-guide.md", "# Cart guide\n\nHow the cart works.\n")
put("src/discart.js", "// discart\n")
put("cart/index.js", "export * from '../src/cart.js';\n")
put("carousel.js", "// carousel\n")

# Binary files
with zipfile.ZipFile("data.zip", "w") as z:
    z.writestr("inside.txt", "hello from inside the zip\n")
put("sheet.xlsx", open("data.zip", "rb").read())
put("blob.bin", bytes(range(256)) * 16)

# Pictures
def magick(*args):
    subprocess.run(["convert", *args], check=True)
magick("-size", "200x120", "xc:red", "-fill", "white", "-pointsize", "40", "-gravity", "center", "-annotate", "0", "TEST", "test.png")
magick("-size", "6000x4000", "gradient:blue-yellow", "-fill", "black", "-pointsize", "500", "-gravity", "center", "-annotate", "0", "BIG", "big.png")
magick("-size", "300x200", "xc:green", "-fill", "white", "-pointsize", "60", "-gravity", "center", "-annotate", "0", "CMYK", "-colorspace", "CMYK", "cmyk.jpg")
magick("-size", "3000x2000", "xc:purple", "-fill", "white", "-pointsize", "300", "-gravity", "center", "-annotate", "0", "WEBP", "photo.webp")

# PDFs
def pdf(texts, count=None):
    objs = [None, "<< /Type /Catalog /Pages 2 0 R >>", None, "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"]
    kids = []
    for t in texts:
        body = "BT /F1 72 Tf 120 400 Td (%s) Tj ET" % t
        objs.append("<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 3 0 R >> >> /Contents %d 0 R >>" % (len(objs) + 1))
        kids.append("%d 0 R" % (len(objs) - 1))
        objs.append("<< /Length %d >>\nstream\n%s\nendstream" % (len(body), body))
    objs[2] = "<< /Type /Pages /Kids [%s] /Count %d >>" % (" ".join(kids), count if count is not None else len(texts))
    out, offs = "%PDF-1.4\n", []
    for i in range(1, len(objs)):
        offs.append(len(out))
        out += "%d 0 obj\n%s\nendobj\n" % (i, objs[i])
    x = len(out)
    out += "xref\n0 %d\n0000000000 65535 f \n" % len(objs) + "".join("%010d 00000 n \n" % o for o in offs)
    out += "trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (len(objs), x)
    return out.encode("latin-1")
put("long.pdf", pdf(["Page %d" % i for i in range(1, 26)]))
put("liar.pdf", pdf(["Liar page %d" % i for i in range(1, 13)], count=3))
put("fake.pdf", "this is not really a PDF\n")
subprocess.run([sys.executable, "-c", "import pypdf, sys\nw = pypdf.PdfWriter()\nw.add_blank_page(612, 792)\nw.encrypt('secret')\nw.write(sys.argv[1])", "locked.pdf"], check=True)

# A notebook with a chart
chart = subprocess.run(["convert", "-size", "240x160", "xc:white", "-fill", "steelblue", "-draw", "rectangle 20,110 60,150", "-draw", "rectangle 90,70 130,150", "-draw", "rectangle 160,30 200,150", "png:-"], check=True, capture_output=True).stdout
nb = {"cells": [
    {"cell_type": "markdown", "metadata": {}, "source": ["# Sales by month\n"]},
    {"cell_type": "code", "execution_count": 1, "metadata": {}, "source": ["sales = [10, 20, 30]\n", "print('total', sum(sales))\n", "plot(sales)"],
     "outputs": [{"output_type": "stream", "name": "stdout", "text": ["total 60\n"]},
                 {"output_type": "display_data", "metadata": {}, "data": {"image/png": base64.b64encode(chart).decode(), "text/plain": ["<Figure: 3 bars>"]}}]}],
    "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3"}}, "nbformat": 4, "nbformat_minor": 5}
put("nb.ipynb", json.dumps(nb, indent=1))
print("made the test files")
