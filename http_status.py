#!/usr/bin/env python3
"""http_status - HTTP status code reference."""
import sys, argparse, json

CODES = {100:"Continue",101:"Switching Protocols",200:"OK",201:"Created",204:"No Content",301:"Moved Permanently",302:"Found",304:"Not Modified",400:"Bad Request",401:"Unauthorized",403:"Forbidden",404:"Not Found",405:"Method Not Allowed",408:"Request Timeout",409:"Conflict",410:"Gone",418:"I'm a Teapot",429:"Too Many Requests",500:"Internal Server Error",502:"Bad Gateway",503:"Service Unavailable",504:"Gateway Timeout"}

CATEGORIES = {1:"Informational",2:"Successful",3:"Redirection",4:"Client Error",5:"Server Error"}

def main():
    p = argparse.ArgumentParser(description="HTTP status codes")
    p.add_argument("code", nargs="?", help="Status code or category (1xx-5xx)")
    p.add_argument("--list", action="store_true")
    args = p.parse_args()
    if args.list:
        print(json.dumps({str(k): v for k, v in sorted(CODES.items())}, indent=2))
    elif args.code:
        if args.code.endswith("xx"):
            cat = int(args.code[0])
            filtered = {k: v for k, v in CODES.items() if k // 100 == cat}
            print(json.dumps({"category": CATEGORIES.get(cat, "Unknown"), "codes": {str(k): v for k, v in sorted(filtered.items())}}, indent=2))
        else:
            code = int(args.code)
            print(json.dumps({"code": code, "message": CODES.get(code, "Unknown"), "category": CATEGORIES.get(code // 100, "Unknown")}))
    else: p.print_help()

if __name__ == "__main__": main()
