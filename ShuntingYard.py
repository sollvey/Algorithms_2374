class ShuntingYard:

    def __init__(self, string, sep=" "):
        self.tokens = string.split(sep)[::-1]
        self.operators = {'+': (2, 'L'), '-': (2, 'L'), '*': (3, 'L'), '/': (3, 'L'), '^': (4, 'R'), '~': (0, 'L')}
        self.functions = ("sin", "cos")
        self.stack = []
        self.answer = []

    def execute(self):
        while self.tokens:
            next_token = self.tokens.pop()
            if next_token.isdigit():
                self.answer.append(next_token)
            elif next_token in self.functions:
                self.stack.append(next_token)
            elif next_token in self.operators:
                while (
                    self.peek() != '('
                    and (
                        self.operators[self.peek()][0] > self.operators[next_token][0]
                        or (
                            self.operators[self.peek()][0] == self.operators[next_token][0]
                            and self.operators[next_token][1] == 'L'
                        )
                    )
                ):
                    self.answer.append(self.stack.pop())
                self.stack.append(next_token)
            elif next_token == '(':
                self.stack.append(next_token)
            elif next_token == ')':
                while self.peek() != '(':
                    # if len(self.stack) == 0:
                    #     print('There are mismatched parentheses')
                    self.answer.append(self.stack.pop())
                # if self.peek() == '(':
                #     print('There are mismatched parentheses')
                self.stack.pop()
                if self.peek() in self.functions:
                    self.answer.append(self.stack.pop())
        
        while self.peek() != '~':
            # if self.peek() != '(':
            #     print('There are mismatched parentheses')
            self.answer.append(self.stack.pop())

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return '~'
                

ShuntingYard("( sin ( 1 / ( 2 * 3 ) ) + 4 ) - 5", sep=" ")