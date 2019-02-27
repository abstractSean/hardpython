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
        (r"^=",                      "EQUAL"),
    ]

@pytest.fixture
def code():
    return [
        "def hello(x, y):",
        "    print(x + y)",
        "hello(10, 20)"
        "x = 10 + 14",
    ]

def test_grammar_tokens():
    function = FuncDef('function', 'parameters', 'body')
    printed = function.__repr__()
    assert printed == ('FuncDef(FUNCDEF,' +
    '\nfunction,'
    '\nparameters,'
    '\nbody)')

@pytest.fixture
def parser(tokens, code):
    parser = Parser(tokens)
    parser.parse(code)
    return parser

def test_analyzer(parser):
    world = World()
    analyzer = Analyzer(parser.grammar_tokens, world)
    analyzer.analyze()
