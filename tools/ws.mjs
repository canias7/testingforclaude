// Tiny WebSocket test server: node tools/ws.mjs [port]
// /basic: text "hello", a binary frame, then close 1000 "bye". /big: one 1.2 MiB text message. /flood: 5000 short messages.
import http from "node:http"; import crypto from "node:crypto";
const port = Number(process.argv[2] || 8765);
const frame = (op, buf) => { const n = buf.length; let h; if (n < 126) h = Buffer.from([0x80 | op, n]); else if (n < 65536) { h = Buffer.alloc(4); h[0] = 0x80 | op; h[1] = 126; h.writeUInt16BE(n, 2); } else { h = Buffer.alloc(10); h[0] = 0x80 | op; h[1] = 127; h.writeBigUInt64BE(BigInt(n), 2); } return Buffer.concat([h, buf]); };
const s = http.createServer((q, r) => { r.end("ws test server\n"); });
s.on("upgrade", (q, sock) => {
  const key = q.headers["sec-websocket-key"]; const acc = crypto.createHash("sha1").update(key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").digest("base64");
  const proto = (q.headers["sec-websocket-protocol"] || "").split(",")[0].trim();
  console.log("connect", q.url, "protocols:", q.headers["sec-websocket-protocol"] || "(none)");
  sock.write("HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: " + acc + "\r\n" + (proto ? "Sec-WebSocket-Protocol: " + proto + "\r\n" : "") + "\r\n");
  sock.on("error", () => {});
  const close = (code, why) => { const b = Buffer.alloc(2 + Buffer.byteLength(why)); b.writeUInt16BE(code, 0); b.write(why, 2); sock.write(frame(8, b)); setTimeout(() => sock.end(), 300); };
  if (q.url.startsWith("/big")) { sock.write(frame(1, Buffer.from("B".repeat(1.2 * 1024 * 1024)))); setTimeout(() => close(1000, "bye"), 2000); }
  else if (q.url.startsWith("/flood")) { let i = 0; const t = setInterval(() => { for (let k = 0; k < 200 && i < 5000; k++) sock.write(frame(1, Buffer.from("line " + i++))); if (i >= 5000) { clearInterval(t); setTimeout(() => close(1000, "done"), 1000); } }, 10); }
  else { sock.write(frame(1, Buffer.from("hello proto=" + (proto || "none")))); setTimeout(() => sock.write(frame(2, Buffer.from([1, 2, 3, 4]))), 500); setTimeout(() => close(1000, "bye"), 1500); }
});
s.listen(port, "127.0.0.1", () => console.log("listening", port));
