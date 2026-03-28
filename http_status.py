#!/usr/bin/env python3
"""http_status - HTTP status code reference."""
import sys
CODES={100:"Continue",101:"Switching Protocols",200:"OK",201:"Created",204:"No Content",
    301:"Moved Permanently",302:"Found",304:"Not Modified",307:"Temporary Redirect",308:"Permanent Redirect",
    400:"Bad Request",401:"Unauthorized",403:"Forbidden",404:"Not Found",405:"Method Not Allowed",
    408:"Request Timeout",409:"Conflict",410:"Gone",413:"Payload Too Large",415:"Unsupported Media Type",
    418:"I'm a Teapot",422:"Unprocessable Entity",429:"Too Many Requests",451:"Unavailable For Legal Reasons",
    500:"Internal Server Error",502:"Bad Gateway",503:"Service Unavailable",504:"Gateway Timeout"}
CATS={"1xx":"Informational","2xx":"Success","3xx":"Redirection","4xx":"Client Error","5xx":"Server Error"}
if __name__=="__main__":
    if len(sys.argv)<2:
        for cat,desc in CATS.items():
            print(f"\n{cat} — {desc}")
            for code,name in sorted(CODES.items()):
                if str(code).startswith(cat[0]):print(f"  {code} {name}")
    else:
        code=int(sys.argv[1])
        if code in CODES:print(f"{code} {CODES[code]}")
        else:print(f"{code} Unknown")
