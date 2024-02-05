import csv 

employee = open('employee_data.csv','r')

csv_file = csv.reader(employee)

              
              

next(csv_file)
num = 0
#write new lines
for rec in csv_file:
    salary = int(rec[3])
    bonus = float(rec[7])
    total_bonus = (salary * bonus)
    total = salary + total_bonus
    print(f" Name:   {rec[1]}")
    print(f" Salary: ${salary}")
    print(f" Bonus:  ${total_bonus}")
    print(f" Pay:    ${total}")
    input()
