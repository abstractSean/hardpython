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
                    i += end
                    self.script.append(Token(token, string, i, end))

