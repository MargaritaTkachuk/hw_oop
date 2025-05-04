from RationalList import RationalList
from Rational import Rational

def list_of_nums(line):
    nums = RationalList()
    for el in line.strip().split():
        try:
            nums += Rational(int(el))
        except ValueError:
            nums += Rational(el)
    return nums

def read_file(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            if line == '\n':
                continue
            try:
                data.append([line, list_of_nums(line)])
            except IndexError:
                continue
    return data

######################### main prog ##############################

with open('output_2.txt', 'wt') as f:
    for data in read_file('input02.txt'):
        print('Cписок:', data[0], file=f)
        print('Сума:', data[1].to_sun_rationals(), f'або {data[1].to_sun_rationals()()}', file=f)
        print(file=f)

# line = '25  -4/4  12/10  13/4  -4  '
# print(line.strip().split())
# print()
# smth = list_of_nums(line)
# print(smth.to_sun_rationals())



