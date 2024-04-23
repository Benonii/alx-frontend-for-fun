#!/usr/bin/python3

''' Markdown 2 HTML '''

import sys
import os


args = sys.argv
if len(args) != 3:
    print("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

if os.path.exists(args[1]):
    sys.exit(0)
else:
    print(f"Missing {args[1]}")
    sys.exit(1)
