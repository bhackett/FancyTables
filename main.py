# https://www.youtube.com/watch?v=Smf68icE_as
from tabulate import tabulate

table_data = [['Name', 'Age', 'Job'],
              ['Mike', '22', 'Programmer'],
              ['John', '24', 'Teacher'],
              ['Jane', '23', 'Designer'],
              ['Jack', '25', 'Manager'],
              ['Brian Hackett', '26', 'Programmer']]

print(tabulate(table_data, headers='firstrow', tablefmt='html'))

with open('mytable.html', 'w') as f:
    f.write(tabulate(table_data, headers="firstrow", tablefmt="html"))
