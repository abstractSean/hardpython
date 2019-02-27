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
        self.tokens = list()
        self.TOKENS = list()

        for token in tokens:
            self.TOKENS.append(
                (re.compile(token[0]), token[1])
            )

    def scan_match(self, i, line):
        start = line[i:]
        for regex, token in self.TOKENS:
            match = regex.match(start)
            if match:
                begin, end = match.span()
                return token, start[:end], end
        return None, start, None

    def scan(self, code):
        self._original_code = code
        for line in code:
            i = 0
            while i < len(line):
                token, string, end = self.scan_match(i, line)
                assert token, "Failed to match line %s" % string
                if token:
                    if string != ' ':
                        self.tokens.append(Token(token, string, i, i+end))
                    i += end
        self.original_tokens = self.tokens

    def match(self, token):
        if self.tokens[0].token == token:
            result = self.tokens[0]
            self.tokens = self.tokens[1:]
            return result
        else:
            assert False, "Failed to match {}".format(token)

    def peek(self):
        for token in self.TOKENS:
            try:
                if self.tokens[0].token == token[1]:
                    return self.tokens[0]
            except IndexError:
                return None
        assert False, "Failed to peak any tokens"

    def push(self, token):
        self.tokens.insert(0, token)

    def skip(self):
        self.tokens = self.tokens[1:]

    def print_tokens(self):
        for token in self.tokens:
            logging.debug(token)
