class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        current_char , previous_char = '+' , '+'
        num = 0

        for i , ch in enumerate(s):
            if ch.isdigit() :
                num = num * 10 + int(ch)

            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1 :
                current = num
                num = 0
                match previous_char :
                    case '+' :
                        stack.append(current)
                    case '-' :
                        stack.append(-current)
                    case '*' :
                        last = stack.pop()
                        stack.append(last * current)
                    case '/':
                        last = stack.pop()
                        stack.append(int(last/current))
                    case _:
                        pass
                previous_char = ch
        return sum(stack)