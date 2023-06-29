"""Запускаем программу
    Для выхода из цикла ctrl+d"""

import sys

employees = {}
for line in sys.stdin:

    line = line.split()

    employee, hours = ' '.join(line[:-1]), int(line[-1])
    if employee not in employees:
        employees[employee] = [hours]
    else:
        employees[employee].append(hours)

for employee, hours in employees.items():
    values_str = ', '.join(str(value) for value in hours)
    print(f'{employee}: {values_str}; sum: {sum(hours)}')
