# arr = [7, 0, 9, 13, 11, 4, 1]

def find_matching_paranthesis(statement, pointer, find):
    weights = {'[': 1, ']': -1}
    balance, traverse = weights[statement[pointer]], []
    if find == '[':
        traverse = range(pointer - 1, -1, -1)
    elif find == ']':
        traverse = range(pointer + 1, len(statement), 1)
    for index in traverse:
        balance += weights.get(statement[index], 0)
        if balance == 0:
            return index


def run(program):
    arr = [0] * 30000
    print(program)
    arr_pointer = 0
    statement_pointer = 0

    while statement_pointer < len(program):
        if program[statement_pointer] == '+':
            arr[arr_pointer] += 1
        elif program[statement_pointer] == '-':
            arr[arr_pointer] -= 1
        elif program[statement_pointer] == '>':
            arr_pointer += 1
        elif program[statement_pointer] == '<':
            arr_pointer -= 1
        elif program[statement_pointer] == '.':
            print(chr(arr[arr_pointer]))
        elif program[statement_pointer] == ',':
            arr[arr_pointer] = input()
        elif program[statement_pointer] == '[':
            if arr[arr_pointer] == 0:
                statement_pointer = find_matching_paranthesis(program, statement_pointer, ']')
                continue
        elif program[statement_pointer] == ']':
            if arr[arr_pointer] != 0:
                statement_pointer = find_matching_paranthesis(program, statement_pointer, '[')
                continue
        statement_pointer += 1


if __name__ == '__main__':
    # program = input()
    program = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
    run(program)
