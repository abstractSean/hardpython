import logging

from .scanner import Scanner


class GrammarToken:

    def __init__(self):
        self.type = None
        self.name = None
        self.params = None
        self.left = None
        self.right = None

    def __repr__(self):
        string = '{}({}'.format(self.__class__.__name__,
                                self.type)
        if self.name:
            string += ', {}'.format(self.name)
        if self.params:
            string += ', {}'.format(self.params)
        if self.left:
            string += ', {}'.format(self.left)
        if self.right:
            string += ', {}'.format(self.right)

        string += ')'
        return string


class FuncDef(GrammarToken):

    def __init__(self, name, params):
        super().__init__()
        self.type = 'FUNCDEF'
        self.name = name
        self.params = params

    def __repr__(self):
        return super().__repr__()


class FuncCall(GrammarToken):

    def __init__(self, name, params):
        super().__init__()
        self.type = 'FUNCCALL'
        self.name = name
        self.params = params

    def __repr__(self):
        return super().__repr__()


class Plus(GrammarToken):

    def __init__(self, left, right):
        super().__init__()
        self.type = 'PLUS'
        self.left = left
        self.right = right

    def __repr__(self):
        return super().__repr__()


class Parser:

    def __init__(self, tokens):
        self.scanner = Scanner(tokens)
        self.grammar_tokens = list()

    def parse(self, code):
        self.scanner.scan(code)

        while self.scanner.tokens:
            self.grammar_tokens.append(self.root())
            logging.debug(self.grammar_tokens)

    def root(self):
        first = self.scanner.peek()

        if first.token == 'DEF':
            return self.function_definition()
        elif first.token == 'INDENT':
            self.scanner.match('INDENT')
        elif first.token == 'NAME':
            name = self.scanner.match('NAME')
            second = self.scanner.peek()

            if second.token == 'LPAREN':
                logging.debug(str(second))
                return self.function_call(name)
            else:
                assert False, 'Not a FUNCDEF or FUNCCALL'

    def function_definition(self):
        self.scanner.skip()
        name = self.scanner.match('NAME')
        self.scanner.match('LPAREN')
        params = self.parameters()
        self.scanner.match('RPAREN')
        self.scanner.match('COLON')
        return FuncDef(name, params)

    def function_call(self, name):
        self.scanner.match('LPAREN')
        params = self.parameters()
        self.scanner.match('RPAREN')
        return FuncCall(name, params)

    def parameters(self):
        params = []
        start = self.scanner.peek()
        while start.token != 'RPAREN':
            params.append(self.expression())
            start = self.scanner.peek()

            logging.debug(str(start))
            if start.token != 'RPAREN':
                assert self.scanner.match('COMMA')
        return params

    def expression(self):
        start = self.scanner.peek()
        if start.token == 'NAME':
            name = self.scanner.match('NAME')
            nxt = self.scanner.peek()
            if nxt.token == 'PLUS':
                return self.plus(name)
            else:
                logging.debug(name)
                return name
        elif start.token == 'INTEGER':
            number = self.scanner.match('INTEGER')
            nxt = self.scanner.peek()
            if nxt.token == 'PLUS':
                return self.plus(number)
            else:
                return number
        else:
            assert False, "Syntax error %s" % start.string

    def plus(self, left):
        self.scanner.match('PLUS')
        right = self.expression()
        return Plus(left, right)
