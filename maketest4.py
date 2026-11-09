import json, os

W = "the quick brown fox jumps over the lazy dog near a quiet river bank".split()
open("part.txt", "w").write("".join("part line %d: %s\n" % (n, " ".join(W[(n + i) % len(W)] for i in range(14))) for n in range(1, 1501)))
open("plain.txt", "w").write("original plain text\n")
open("old.txt", "wb").write(b"caf\xe9 au lait\n")
open("u16.txt", "wb").write(b"\xff\xfe" + "héllo utf16\n".encode("utf-16-le"))
open("bom.txt", "wb").write(b"\xef\xbb\xbfhello\n")
open("target.txt", "w").write("target original\n")
open("mod.txt", "w").write("mod line one\n")
open("touch.txt", "w").write("touch line one\n")
open("tab.py", "w").write("def f():\n\tif True:\n\t\treturn 1\n")
os.makedirs("realdir", exist_ok=True)
open("realdir/keep.txt", "w").write("keeps the folder\n")
os.makedirs("afolder", exist_ok=True)
open("afolder/keep.txt", "w").write("keeps the folder\n")
os.makedirs("sub", exist_ok=True)
open("sub/a.txt", "w").write("a file in sub\n")
open("sub/AGENTS.md", "w").write("".join("Line %d. This text only fills space for a size test; it asks nothing and changes nothing.\n" % n for n in range(1, 701)))
for name, to in (("link.txt", "target.txt"), ("linkdir", "realdir"), ("loopa", "loopb"), ("loopb", "loopa"), ("nowhere", "/nonexistent/dir")):
    if os.path.lexists(name):
        os.remove(name)
    os.symlink(to, name)
open("nb.ipynb", "w").write(json.dumps({"cells": [{"cell_type": "code", "execution_count": 1, "metadata": {}, "source": ["print(1)"],
    "outputs": [{"output_type": "stream", "name": "stdout", "text": ["1\n"]}]}], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}))
print("made the test files; sub/AGENTS.md is", os.path.getsize("sub/AGENTS.md"), "bytes")
