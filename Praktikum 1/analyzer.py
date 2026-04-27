#!/usr/bin/env python3
import cgi
import re

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
code = form.getvalue("code", "")

RESERVED_WORDS = {
    "if", "else", "while", "for", "return",
    "int", "float", "double", "char", "void"
}

TOKEN_REGEX = [
    ("NUMBER", r"\d+(\.\d+)?"),
    ("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("OPERATOR", r"[\+\-\*/=<>!]+"),
    ("SYMBOL", r"[()\{\}\[\];,]"),
    ("WHITESPACE", r"\s+"),
]

def add_unique(lst, item):
    if item not in lst:
        lst.append(item)

def tokenize_and_group(code):
    index = 0
    variables, reserved, operators, symbols, numbers = [], [], [], [], []

    while index < len(code):
        match = None

        for token_type, pattern in TOKEN_REGEX:
            regex = re.compile(pattern)
            match = regex.match(code, index)

            if match:
                text = match.group(0)

                if token_type != "WHITESPACE":
                    if token_type == "IDENTIFIER":
                        if text in RESERVED_WORDS:
                            add_unique(reserved, text)
                        else:
                            add_unique(variables, text)
                    elif token_type == "NUMBER":
                        add_unique(numbers, text)
                    elif token_type == "OPERATOR":
                        add_unique(operators, text)
                    elif token_type == "SYMBOL":
                        add_unique(symbols, text)

                index = match.end()
                break

        if not match:
            index += 1

    return reserved, variables, operators, symbols, numbers

reserved, variables, operators, symbols, numbers = tokenize_and_group(code)

print("<html><body>")
print("<h2>Hasil Analisis</h2>")
print("<p><b>Reserved:</b>", reserved, "</p>")
print("<p><b>Variabel:</b>", variables, "</p>")
print("<p><b>Operator:</b>", operators, "</p>")
print("<p><b>Simbol:</b>", symbols, "</p>")
print("<p><b>Angka:</b>", numbers, "</p>")
print("<br><a href='index.html'>Kembali</a>")
print("</body></html>")