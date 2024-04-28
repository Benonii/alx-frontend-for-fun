#!/usr/bin/python3

''' Markdown 2 HTML '''

import sys
import os
import hashlib


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    elif not os.path.exists(args[1]):
        print(f"Missing {args[1]}")
        sys.exit(1)

    else:
        def parse_markdown(markdown):
            ''' Parses Markdown to convert it to HTML '''
            with open(markdown, "r", encoding="utf-8") as f:
                markdown_lines = f.readlines()
            return markdown_lines

        markdown_lines = parse_markdown(args[1])
        html_content = ""
        unordered_list = []
        ordered_list = []
        paragraph = []
        bold_text = ""
        em_text = ""

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
                unordered_list.append(line)
            elif line.startswith("* "):
                ordered_list.append(line)
            else:
                new_line = ""
                iterator = iter(line)
                for char in iterator:
                    if char == "*" and next(iterator) == "*":
                        index = line.index(char)
                        new_line += "<b>"
                        char = next(iterator)
                        while not (char == "*" and next(iterator) == "*"):
                            new_line += char
                            char = next(iterator)
                        new_line += "</b>"

                    elif char == "_" and next(iterator) == "_":
                        new_line += "<em>"
                        char = next(iterator)
                        while not (char == "_" and next(iterator) == "_"):
                            new_line += char
                            char = next(iterator)
                        new_line += "</em>"
                    elif char == "[" and next(iterator) == "[":
                        to_hash = ""
                        md5 = hashlib.md5()
                        char = next(iterator)
                        while not (char == "]" and next(iterator) == "]"):
                            to_hash += char
                            char = next(iterator)
                        md5.update(to_hash.encode())
                        new_line += md5.hexdigest()
                    elif char == "(" and next(iterator) == "(":
                        char = next(iterator)
                        while not (char == ")" and next(iterator) == ")"):
                            if char not in ['c', 'C']:
                                new_line += char
                            char = next(iterator)

                    else:
                        if char not in ["*", "_", "[", "]", "(", ")"]:
                            new_line += char

                paragraph.append(new_line)

        if unordered_list:
            html_content += "<ul>\n"
            for element in unordered_list:
                new_line = ""
                iterator = iter(element)
                for char in iterator:
                    if char == "*" and next(iterator) == "*":
                        new_line += "<b>"
                        char = next(iterator)
                        # char = next(iterator)
                        while not (char == "*" and next(iterator) == "*"):
                            new_line += char
                            char = next(iterator)
                        new_line += "</b>"
                    elif char == "_" and next(iterator) == "_":
                        new_line += "<em>"
                        char = next(iterator)
                        while not (char == "_" and next(iterator) == "_"):
                            new_line += char
                            char = next(iterator)
                        new_line += "</em>"
                        new_line += "</em>"
                    elif char == "[" and next(iterator) == "[":
                        to_hash = ""
                        md5 = hashlib.md5()
                        char = next(iterator)
                        while not (char == "]" and next(iterator) == "]"):
                            to_hash += char
                            char = next(iterator)
                        md5.update(to_hash.encode())
                        new_line += md5.hexdigest()
                    elif char == "(" and next(iterator) == "(":
                        char = next(iterator)
                        while not (char == ")" and next(iterator) == ")"):
                            if char not in ['c', 'C']:
                                new_line += char
                            char = next(iterator)

                    else:
                        if char not in ["*", "_", "[", "]", "(", ")"]:
                            new_line += char

                html_content += f"<li>{new_line[2:-1]}</li>\n"
            html_content += "</ul>\n"

        if ordered_list:
            html_content += "<ol>\n"
            for element in unordered_list:
                new_line = ""
                iterator = iter(element)
                for char in iterator:
                    if char == "*" and next(iterator) == "*":
                        new_line += "<b>"
                        char = next(iterator)
                        # char = next(iterator)
                        while not (char == "*" and next(iterator) == "*"):
                            new_line += char
                            char = next(iterator)
                        new_line += "</b>"
                    elif char == "_" and next(iterator) == "_":
                        new_line += "<em>"
                        char = next(iterator)
                        while not (char == "_" and next(iterator) == "_"):
                            new_line += char
                            char = next(iterator)
                        new_line += "</em>"
                    elif char == "[" and next(iterator) == "[":
                        to_hash = ""
                        md5 = hashlib.md5()
                        char = next(iterator)
                        while not (char == "]" and next(iterator) == "]"):
                            to_hash += char
                            char = next(iterator)
                        md5.update(to_hash.encode())
                        new_line += md5.hexdigest()
                    elif char == "(" and next(iterator) == "(":
                        char = next(iterator)
                        while not (char == ")" and next(iterator) == ")"):
                            if char not in ['c', 'C']:
                                new_line += char
                            char = next(iterator)

                    else:
                        if char not in ["*", "_", "[", "]", "(", ")"]:
                            new_line += char

            for element in ordered_list:
                html_content += f"<li>{new_line[2:-1]}</li>\n"
            html_content += "</ol>\n"

        if paragraph != "":
            html_content += "<p>\n"

            for line in paragraph:
                for char in line:
                    if char == "\n":
                        try:
                            next_line = paragraph[paragraph.index(line) + 1]
                            if next_line == "\n":
                                html_content += "\n</p>\n<p>\n"
                            else:
                                if line == "\n":
                                    continue
                                html_content += "\n<br/>\n"
                        except Exception as e:
                            html_content += "\n</p>\n"
                    else:
                        html_content += char

        if bold_text:
            html_content += f"<b>{bold_text}</b>"
        if em_text:
            html_content += f"<em>{em_text}</em"

        with open(args[2], "w", encoding="utf-8") as f:
            f.write(html_content)
    sys.exit(0)
