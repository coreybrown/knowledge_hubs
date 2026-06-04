// Minimal isolation probe: zero imports, no config. If GET /api/ping also
// fails with FUNCTION_INVOCATION_FAILED, the project's function runtime is the
// problem (not api/ask). Delete once diagnosed.
export default function handler(_req: any, res: any) {
  res.status(200).end("pong");
}
