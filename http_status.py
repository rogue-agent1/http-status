#!/usr/bin/env python3
"""http_status - HTTP status code reference and lookup."""
import sys
CODES = {
100:'Continue',101:'Switching Protocols',200:'OK',201:'Created',202:'Accepted',204:'No Content',
301:'Moved Permanently',302:'Found',304:'Not Modified',307:'Temporary Redirect',308:'Permanent Redirect',
400:'Bad Request',401:'Unauthorized',403:'Forbidden',404:'Not Found',405:'Method Not Allowed',
408:'Request Timeout',409:'Conflict',410:'Gone',413:'Payload Too Large',415:'Unsupported Media Type',
418:"I'm a Teapot",422:'Unprocessable Entity',429:'Too Many Requests',
500:'Internal Server Error',501:'Not Implemented',502:'Bad Gateway',503:'Service Unavailable',504:'Gateway Timeout',
}
CATS = {1:'ℹ️  Informational',2:'✅ Success',3:'↪️  Redirection',4:'❌ Client Error',5:'💥 Server Error'}

def main():
    args = sys.argv[1:]
    if not args or '-h' in args:
        print("Usage: http_status.py [CODE|CATEGORY|all|search TERM]"); return
    if args[0] == 'all' or args[0] == 'list':
        for code in sorted(CODES):
            cat = CATS.get(code//100,'')
            print(f"  {code} {CODES[code]}")
    elif args[0] == 'search':
        term = ' '.join(args[1:]).lower()
        for code, desc in sorted(CODES.items()):
            if term in desc.lower() or term in str(code):
                print(f"  {code} {desc}")
    elif args[0].isdigit() and len(args[0]) == 1:
        cat = int(args[0])
        print(CATS.get(cat, ''))
        for code, desc in sorted(CODES.items()):
            if code // 100 == cat: print(f"  {code} {desc}")
    else:
        code = int(args[0])
        desc = CODES.get(code, 'Unknown')
        cat = CATS.get(code//100, '')
        print(f"{cat}\n  {code} {desc}")

if __name__ == '__main__': main()
