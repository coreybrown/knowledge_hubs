// Isolation probe (temporary): plain CommonJS, native res, zero imports.
// If GET /api/ping returns "pong", the Node function runtime works and the
// earlier crashes were the TypeScript build. Delete once /api/ask is verified.
module.exports = (req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain; charset=utf-8");
  res.end("pong");
};
