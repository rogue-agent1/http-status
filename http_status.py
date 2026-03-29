#!/usr/bin/env python3
"""HTTP status code reference."""

CODES = {
    100: ("Continue", "informational"), 101: ("Switching Protocols", "informational"),
    200: ("OK", "success"), 201: ("Created", "success"), 204: ("No Content", "success"),
    301: ("Moved Permanently", "redirect"), 302: ("Found", "redirect"),
    304: ("Not Modified", "redirect"), 307: ("Temporary Redirect", "redirect"),
    400: ("Bad Request", "client_error"), 401: ("Unauthorized", "client_error"),
    403: ("Forbidden", "client_error"), 404: ("Not Found", "client_error"),
    405: ("Method Not Allowed", "client_error"), 409: ("Conflict", "client_error"),
    429: ("Too Many Requests", "client_error"),
    500: ("Internal Server Error", "server_error"), 502: ("Bad Gateway", "server_error"),
    503: ("Service Unavailable", "server_error"), 504: ("Gateway Timeout", "server_error"),
}

def lookup(code):
    if code in CODES:
        name, cat = CODES[code]
        return {"code": code, "name": name, "category": cat}
    return {"code": code, "name": "Unknown", "category": classify(code)}

def classify(code):
    if 100 <= code < 200: return "informational"
    if 200 <= code < 300: return "success"
    if 300 <= code < 400: return "redirect"
    if 400 <= code < 500: return "client_error"
    if 500 <= code < 600: return "server_error"
    return "unknown"

def is_success(code): return 200 <= code < 300
def is_redirect(code): return 300 <= code < 400
def is_client_error(code): return 400 <= code < 500
def is_server_error(code): return 500 <= code < 600
def is_error(code): return code >= 400

def by_category(category):
    return {c: n for c, (n, cat) in CODES.items() if cat == category}

if __name__ == "__main__":
    import sys
    code = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    info = lookup(code)
    print(f"{info['code']} {info['name']} ({info['category']})")

def test():
    assert lookup(200)["name"] == "OK"
    assert lookup(404)["name"] == "Not Found"
    assert lookup(999)["name"] == "Unknown"
    assert classify(200) == "success"
    assert classify(404) == "client_error"
    assert classify(500) == "server_error"
    assert is_success(200) and not is_success(404)
    assert is_error(500) and is_error(400) and not is_error(200)
    assert is_redirect(301) and not is_redirect(200)
    errors = by_category("client_error")
    assert 404 in errors
    assert 200 not in errors
    print("  http_status: ALL TESTS PASSED")
