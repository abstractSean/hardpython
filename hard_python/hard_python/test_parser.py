import pytest

from .parser import *

@pytest.fixture
def tokens():
    return [
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

@pytest.fixture
def code():
    return [
        "def hello(x, y):",
        "    print(x + y)",
        "hello(10, 20)",
    ]

def test_grammar_tokens():
    function = FuncDef('function', 'parameters')
    printed = function.__repr__()
    assert printed == 'FuncDef(FUNCDEF, function, parameters)'

def test_parser(tokens, code):
    parser = Parser(tokens)
    parser.parse(code)


