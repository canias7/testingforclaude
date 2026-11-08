import os, subprocess, sys

def put(path, data):
    with open(path, "wb") as f:
        f.write(data if isinstance(data, bytes) else data.encode())

def line(target):
    words, i = [], 0
    while len(" ".join(words)) < target:
        i += 1
        words.append("w%d" % i)
    return " ".join(words)[:target]

if sys.argv[1:] == ["scratch"]:
    os.makedirs("/tmp/coder-scratch", exist_ok=True)
    if os.path.lexists("/tmp/coder-scratch/link.txt"):
        os.remove("/tmp/coder-scratch/link.txt")
    os.symlink("/etc/hostname", "/tmp/coder-scratch/link.txt")
    print("made /tmp/coder-scratch/link.txt, a link to /etc/hostname")
    sys.exit(0)

put("longline.txt", "first line\n" + line(5000) + "\nthird line\n")
put("line20k.txt", "first\n" + line(20000) + "\nlast\n")
put("hugeline.txt", "first\n" + "y" * 150000 + "\nlast\n")
put("notes.txt", "apple\nbanana\ncherry\n")

def magick(*args):
    subprocess.run(["convert", *args], check=True)
magick("-size", "6000x4000", "gradient:blue-yellow", "-fill", "black", "-pointsize", "500", "-gravity", "center", "-annotate", "0", "BIG", "big.png")
for kind, colour, word in (("gif", "orange", "GIF"), ("bmp", "teal", "BMP"), ("tif", "maroon", "TIFF")):
    magick("-size", "300x200", "xc:" + colour, "-fill", "white", "-pointsize", "60", "-gravity", "center", "-annotate", "0", word, "pic." + kind)
print("made the test files")
