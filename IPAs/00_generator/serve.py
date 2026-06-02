#!/usr/bin/env python3
"""Tiny static server for the generated IPA site."""
import http.server
import socketserver
import pathlib

SITE = pathlib.Path(__file__).resolve().parent.parent / "site"
PORT = 8765


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SITE), **kwargs)

    def log_message(self, *args):
        pass


with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print(f"Serving {SITE} at http://127.0.0.1:{PORT}")
    httpd.serve_forever()
