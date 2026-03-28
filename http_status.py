#!/usr/bin/env python3
"""HTTP status code reference — lookup and categorize."""
import sys
CODES={100:"Continue",101:"Switching Protocols",200:"OK",201:"Created",204:"No Content",301:"Moved Permanently",302:"Found",304:"Not Modified",400:"Bad Request",401:"Unauthorized",403:"Forbidden",404:"Not Found",405:"Method Not Allowed",408:"Request Timeout",409:"Conflict",410:"Gone",413:"Payload Too Large",415:"Unsupported Media Type",418:"I'm a Teapot",429:"Too Many Requests",500:"Internal Server Error",502:"Bad Gateway",503:"Service Unavailable",504:"Gateway Timeout"}
CAT={1:"Informational",2:"Success",3:"Redirection",4:"Client Error",5:"Server Error"}
def cli():
    if len(sys.argv) < 2:
        for code, desc in sorted(CODES.items()): print(f"  {code} {desc}")
        return
    code = int(sys.argv[1])
    cat = CAT.get(code // 100, "Unknown")
    desc = CODES.get(code, "Unknown Status Code")
    print(f"  {code} {desc}  [{cat}]")
if __name__ == "__main__": cli()
