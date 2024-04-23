#!/usr/bin/python3

''' Markdown 2 HTML '''

import sys
import os


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    if not os.path.exists(args[1]):
        print(f"Missing {args[1]}")
        sys.exit(1)

    def parse_markdown(markdown):
        with open(markdown, "r", encoding="utf-8") as f:
            markdown_lines = f.readlines()
        return markdown_lines

    markdown_lines = parse_markdown(args[1])
    html_content = ""
    list = []
    for line in markdown_lines:
        if line.startswith("# "):
            html_content += f"<h1>{line[2:-1]}</h1>\n"
        elif line.startswith("## "):
            html_content += f"<h2>{line[3:-1]}</h2>\n"
        elif line.startswith("### "):
            html_content += f"<h3>{line[4:-1]}</h3>\n"
        elif line.startswith("#### "):
            html_content += f"<h4>{line[5:-1]}</h4>\n"
        elif line.startswith("##### "):
            html_content += f"<h5>{line[6:-1]}</h5>\n"
        elif line.startswith("###### "):
            html_content += f"<h6>{line[7:-1]}</h6>\n"
        elif line.startswith("- "):
            list.append(line)
        else:
            html_content += f"<p>{line}</p>" + "\n"

    if list:
        html_content += "<ul>\n"
        for element in list:
            html_content += f"<li>{element[2:-1]}</li>\n"
        html_content += "</ul>\n"

    # def write_to_html(html_content, html_file):
    with open(args[2], "w", encoding="utf-8") as f:
        f.write(html_content)
