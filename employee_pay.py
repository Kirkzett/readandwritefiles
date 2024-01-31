import csv 

employee = open('employee_data.csv','r')

csv_file = csv.reader(employee)

print("Name, Age, Salary, Hours, Productivity, Team, Bonus" + "\n")
              
              

next(csv_file)
num = 0
#write new lines
for rec in csv_file:
    print(f"Name: {rec[1]}")
    print(f"Salary: $ {rec[2]:2d")
    bonus = float(rec[7])
    salary = float(rec[3])
    bonus_calc = salary + (salary * bonus)
    print(f"{rec[1]}, {rec[2]}, {rec[3]}, {rec[4]}, {rec[5]}, {rec[6]}, {bonus_calc} \n")
    input()
    num += 1

print(f"Total Cusotmers: {num}")