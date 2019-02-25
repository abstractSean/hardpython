import pytest

from .scanner import Scanner
from .scanner import Token

@pytest.fixture
def scanner():
    tokens = [
        (r"^def",                    "DEF"),
        (r"^[a-zA-Z_][a-zA-Z0-9_]*", "NAME"),
        (r"^[0-9]+",                 "INTEGER"),
        (r"^\(",                     "LPAREN"),
        (r"^\)",                     "RPAREN"),
        (r"^\+",                     "PLUS"),
        (r"^:",                      "COLON"),
        (r"^,",                      "COMMA"),
        (r"^\s{4}",                  "INDENT"),
        (r"^\s",                     "SPACE"),
    ]
    return Scanner(tokens)

@pytest.fixture
def code():
    return [
        "def hello(x, y):",
        "    print(x + y)",
        "hello(10, 20)",
    ]

def test_scan(scanner, code):
    scanner.scan(code)
    peak = scanner.peak()
    assert peak == Token('DEF', 'def', 0, 3)
    match = scanner.match('DEF')
    assert match == Token('DEF', 'def', 0, 3)
    peak = scanner.peak()
    assert peak == Token('SPACE', ' ', 3, 4)
    scanner.skip()
    assert scanner.peak() == Token('NAME', 'hello', 4, 9)
    scanner.push(peak)
    assert scanner.peak()  == Token('SPACE', ' ', 3, 4)

