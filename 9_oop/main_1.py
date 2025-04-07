from Rational import Rational

def solve(line):
    lst = line.split()
    list_rational = []
    list_operators = []

    for el in lst:
        if el in '-+*':
            list_operators.append(el)
        else:
            list_rational.append(el)

    for i in range(len(list_rational)):
        try:
            list_rational[i] = int(list_rational[i])
        except ValueError:
            continue

    i = 0
    while i < len(list_operators):
        if list_operators[i] == '*':
            result = Rational(list_rational[i]) * Rational(list_rational[i + 1])
            list_rational[i:i + 2] = [result]
            list_operators.pop(i)
        else:
            i += 1

    res = Rational(list_rational[0])
    for rational, operator in zip(list_rational[1:], list_operators):
        num = Rational(rational)
        if operator == '-':
            res -= num
        elif operator == '+':
            res += num

    return line, str(res)


def solve_for_file(filename):
    sols = []
    with open(filename, 'r') as f:
        for line in f:
            try:
                if line.strip():
                    sols.append(solve(line.strip()))
            except IndexError:
                continue

    return sols



############## main prog ##############
# print(solve_for_file('input01 (3).txt'))

with open('output.txt', 'wt') as f:
    for solution in solve_for_file('input01 (3).txt'):
        print('Вираз:', solution[0], file=f)
        print('Значення:', solution[1], f'або {Rational(solution[1])()}', file=f)
        print(file=f)
