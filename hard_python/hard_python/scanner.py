import logging
import re


class Token:

    def __init__(self, token, string, begin, end):
        self.token = token
        self.string = string
        self.begin = begin
        self.end = end

    def __eq__(self, token):
        if (self.token == token.token and
            self.string == token.string and
            self.begin == token.begin and
            self.end == token.end):
            return True
        else:
            return False

    def __repr__(self):
        return 'Token({}, {}, {}, {})'.format(
            self.token,
            self.string,
            self.begin,
            self.end,
        )

class Scanner:

    def __init__(self, tokens):
        self.script = list()
        self.TOKENS = list()

        for token in tokens:
            self.TOKENS.append(
                (re.compile(token[0]), token[1])
            )

    def match(self, i, line):
        start = line[i:]
        for regex, token in self.TOKENS:
            match = regex.match(start)
            if match:
                begin, end = match.span()
                return token, start[:end], end
        return None, start, None

    def scan(self, code):
        for line in code:
            i = 0
            while i < len(line):
                token, string, end = self.match(i, line)
                assert token, "Failed to match line %s" % string
                if token:
                    self.script.append(Token(token, string, i, i+end))
                    i += end
        self.print_tokens()

    def print_tokens(self):
        for token in self.script:
            logging.debug(token)
        
