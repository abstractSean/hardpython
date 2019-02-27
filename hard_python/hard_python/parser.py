import logging

from .scanner import Scanner


class Production:

    def __init__(self):
        self.type = None
        self.name = None
        self.params = None
        self.body = None
        self.left = None
        self.right = None

    def analyze(self, world):
        """Implement analyzer here"""
        pass

    def __repr__(self):
        string = '{}({}'.format(self.__class__.__name__,
                                self.type)
        if self.name:
            string += ',\n{}'.format(self.name)
        if self.params:
            string += ',\n{}'.format(self.params)
        if self.body:
            string += ',\n{}'.format(self.body)
        if self.left:
            string += ',\n{}'.format(self.left)
        if self.right:
            string += ',\n{}'.format(self.right)

        string += ')'
        return string


class FuncDef(Production):

    def __init__(self, name, params, body):
        super().__init__()
        self.type = 'FUNCDEF'
        self.name = name
        self.params = params
        self.body = body

    def __repr__(self):
        return super().__repr__()

    def analyze(self, world):
        logging.debug('> FuncDef: {}'.format(self.name))
        self.params.analyze(world)
        self.body.analyze(world)


class FuncCall(Production):

    def __init__(self, name, params):
        super().__init__()
        self.type = 'FUNCCALL'
        self.name = name
        self.params = params

    def __repr__(self):
        return super().__repr__()

    def analyze(self, world):
        logging.debug('> FuncCall: {}'.format(self.name))
        self.params.analyze(world)


class Parameters(Production):

    def __init__(self, expressions):
        super().__init__()
        self.expressions = expressions

    def analyze(self, world):
        logging.debug('>> Parameters: ')
        for expr in self.expressions:
            expr.analyze(world)


class Expr(Production):
    
    def __init__(self, expression):
        super().__init__()
        self.expression = expression

    def analyze(self, world):
        logging.debug('>>>> Expr: {}'.format(self.expression))

class IntExpr(Production):

    def __init__(self, integer):
        super().__init__()
        self.integer = integer

    def analyze(self, world):
        logging.debug('>>>> IntExpr: {}'.format(self.integer))


class Plus(Production):

    def __init__(self, left, right):
        super().__init__()
        self.type = 'PLUS'
        self.left = left
        self.right = right

    def __repr__(self):
        return super().__repr__()

    def analyze(self, world):
        logging.debug('>>> AddExpr: ')
        self.left.analyze(world)
        self.right.analyze(world)

class Assignment(Production):

    def __init__(self, left, right):
        super().__init__()
        self.type = 'ASSIGNMENT'
        self.left = left
        self.right = right

    def __repr__(self):
        return super().__repr__()

    def analyze(self, world):
        logging.debug('>>> AssignExpr: ')
        self.left.analyze(world)
        self.right.analyze(world)

class Parser:

    def __init__(self, tokens):
        self.scanner = Scanner(tokens)
        self.grammar_tokens = list()

    def parse(self, code):
        self.scanner.scan(code) 
        while self.scanner.tokens:
            self.grammar_tokens.append(self.root())
            #logging.debug(self.grammar_tokens)

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
                #logging.debug(str(second))
                return self.function_call(name)
            elif second.token == 'EQUAL':
                return self.assignment(Expr(name))
            else:
                assert False, 'Not a FUNCDEF or FUNCCALL'

    def function_definition(self):
        self.scanner.skip()
        name = self.scanner.match('NAME')
        self.scanner.match('LPAREN')
        params = self.parameters()
        self.scanner.match('RPAREN')
        self.scanner.match('COLON')
        self.scanner.match('INDENT')
        nxt = self.scanner.peek()
        if nxt.token == 'NAME':
            name = self.scanner.match('NAME')
            nxt = self.scanner.peek()
            if nxt.token == 'LPAREN':
                body = self.function_call(name)
        return FuncDef(name, params, body)

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

            #logging.debug(str(start))
            if start.token != 'RPAREN':
                assert self.scanner.match('COMMA')
        return Parameters(params)

    def expression(self):
        start = self.scanner.peek()
        if start.token == 'NAME':
            name = self.scanner.match('NAME')
            nxt = self.scanner.peek()
            if nxt and nxt.token == 'PLUS':
                return self.plus(Expr(name))
            else:
                #logging.debug(name)
                return Expr(name)
        elif start.token == 'INTEGER':
            number = self.scanner.match('INTEGER')
            nxt = self.scanner.peek()
            if nxt and nxt.token == 'PLUS':
                return self.plus(IntExpr(number))
            else:
                return IntExpr(number)
        else:
            assert False, "Syntax error %s" % start.string

    def plus(self, left):
        self.scanner.match('PLUS')
        right = self.expression()
        return Plus(left, right)

    def assignment(self, left):
        self.scanner.match('EQUAL')
        right = self.expression()
        return Assignment(left, right)

    def print(self):
        for token in self.grammar_tokens:
            logging.debug(token)

class World:
    
    def __init__(self):
        self.variables = list()
        self.functions = dict()

class Analyzer:

    def __init__(self, parse_tree, world):
        self.parse_tree = parse_tree
        self.world = world

    def analyze(self):
        for node in self.parse_tree:
            node.analyze(self.world)
