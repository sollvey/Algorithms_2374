from Stack import Stack


class ShuntingYard:

    def __init__(self, string, sep=" "):
        self.tokens = string.split(sep)[::-1]
        self.operators = {'+': (2, 'L'), '-': (2, 'L'), '*': (3, 'L'), '/': (3, 'L'), '^': (4, 'R'), '~': (0, 'L')}
        self.functions = ("sin", "cos")
        self.stack = Stack()
        self.answer = []

    def execute(self):
        while self.tokens:
            next_token = self.tokens.pop()
            if next_token.isdigit():
                self.answer.append(next_token)
            elif next_token in self.functions:
                self.stack.push(next_token)
            elif next_token in self.operators:
                while (
                    self.stack.peek() != '('
                    and (
                        self.operators[self.stack.peek()][0] > self.operators[next_token][0]
                        or (
                            self.operators[self.stack.peek()][0] == self.operators[next_token][0]
                            and self.operators[next_token][1] == 'L'
                        )
                    )
                ):
                    self.answer.append(self.stack.pop())
                self.stack.push(next_token)
            elif next_token == '(':
                self.stack.push(next_token)
            elif next_token == ')':
                while self.stack.peek() != '(':
                    # if len(self.stack) == 0:
                    #     print('There are mismatched parentheses')
                    self.answer.append(self.stack.pop())
                # if self.stack.peek() == '(':
                #     print('There are mismatched parentheses')
                self.stack.pop()
                if self.stack.peek() in self.functions:
                    self.answer.append(self.stack.pop())
        
        while self.stack.peek() != '~':
            # if self.stack.peek() != '(':
            #     print('There are mismatched parentheses')
            self.answer.append(self.stack.pop())
                
input_string = "( sin ( 1 / ( 2 * 3 ) ) + 4 ) - 5"
print("INPUT:", input_string)
result = ShuntingYard(input_string, sep=" ")
result.execute()
print(f"OUTPUT: {' '.join(result.answer)}")