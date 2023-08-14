import re

class Token:
    def __init__(self, value, type):
        self.value = value
        self.type = type

class TokenPattern:
    def __init__(self, pattern, type):
        self.pattern = pattern
        self.type = type

class TokenType:
    PLUS, MINUS, MULTIPLY, DIV, ASSIGN, OPEN_PAREN, CLOSE_PAREN, NUMBER, IDENTIFIER, KEYWORD = range(10)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        try:
            return self.statement()
        except IndexError:
            return False

    def statement(self):
        return self.assignment() or self.expression()

    def assignment(self):
        if self.match(TokenType.IDENTIFIER) and self.match(TokenType.ASSIGN):
            return self.expression()
        return False

    def expression(self):
        return self.term() and self.expression_tail()

    def expression_tail(self):
        if self.match(TokenType.PLUS) or self.match(TokenType.MINUS):
            return self.term() and self.expression_tail()
        return True

    def term(self):
        return self.factor() and self.term_tail()

    def term_tail(self):
        if self.match(TokenType.MULTIPLY) or self.match(TokenType.DIV):
            return self.factor() and self.term_tail()
        return True

    def factor(self):
        return (self.match(TokenType.NUMBER) or
                self.match(TokenType.IDENTIFIER) or
                self.match(TokenType.KEYWORD) or
                (self.match(TokenType.OPEN_PAREN) and self.expression() and self.match(TokenType.CLOSE_PAREN)))

    def match(self, *types):
        for type in types:
            if self.check(type):
                self.advance()
                return True
        return False

    def check(self, type):
        return self.current < len(self.tokens) and self.tokens[self.current].type == type

    def advance(self):
        self.current += 1

def tokenize_line(line):
    tokens = []
    line = line.strip()

    if line.startswith("//"):
        return tokens

    pos = 0
    while pos < len(line):
        match = None
        for pattern in token_patterns:
            regex = re.compile("^" + pattern.pattern)
            matcher = regex.match(line[pos:])

            if matcher:
                token_value = matcher.group(0)
                tokens.append(Token(token_value, pattern.type))
                pos += len(token_value)
                match = Token(token_value, pattern.type)
                break

        if not match:
            pos += 1
    return tokens

token_patterns = [
    TokenPattern("\\+", TokenType.PLUS),
    TokenPattern("-", TokenType.MINUS),
    TokenPattern("\\*", TokenType.MULTIPLY),
    TokenPattern("/", TokenType.DIV),
    TokenPattern(":=", TokenType.ASSIGN),
    TokenPattern("\\(", TokenType.OPEN_PAREN),
    TokenPattern("\\)", TokenType.CLOSE_PAREN),
    TokenPattern("\\d+(\\.\\d+)?", TokenType.NUMBER),
    TokenPattern("read", TokenType.KEYWORD),
    TokenPattern("write", TokenType.KEYWORD),
    TokenPattern("[a-zA-Z]\\w*", TokenType.IDENTIFIER)
]

def main():
    filename = "code.txt"
    try:
        with open(filename, 'r') as reader:
            lines = reader.readlines()

        line_num = 1
        for line in lines:
            line = line.strip()
            if line and not line.startswith("//"):
                print("\nExpression", line_num, ":", line)
                tokens = tokenize_line(line)
                if tokens:
                    print("Tokens:")
                    for token in tokens:
                        print(f"   '{token.value}', Category: {token.type}")
                    parser = Parser(tokens)
                    if parser.parse():
                        print("Result: Expression is valid.\n")
                    else:
                        print("Result: Expression is invalid.\n")
            line_num += 1

    except IOError as e:
        print(e)

if __name__ == "__main__":
    main()
