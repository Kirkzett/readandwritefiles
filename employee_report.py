import csv

employee = open('employee_data.csv', 'r')

csv_file = csv.reader(employee)

#intialize efficency lists
high_eff = []
low_eff = []

#initialize age lists from 20-40
age_forty = []
age_thrity = []
age_twenty = []

#skip header
next(csv_file)

for rec in csv_file:
    #sparce 
    hours = int(rec[4])
    productivity = int(rec[5])
    name = rec[1]
    age = int(rec[2])
    efficency =  productivity / hours

    #conditions for appending efficency lists
    if efficency > 2:
        high_eff.append(name)
    elif efficency < 1:
        low_eff.append(name)

    #conditions for appending age lists
    if age >= 40:      #and age < 50
        age_forty.append(name)
    elif age >= 30:     # and age < 40
        age_thrity.append(name)
    elif age >= 20:    #and age < 30
        age_twenty.append(name)
    
print('Highly Efficent Individuals:')   
for name in high_eff:
    print(name)
    
print()

print('Low Efficency Individuals')
for name in low_eff:
    print(name)

print()

x = 0
print("Employees in their 40's")
for name in age_forty:
    print(name)
    x += 1
print(f"Total number of employees in their 40's: {x}")

print()

y = 0
print("Employees in their 30's")
for name in age_thrity:
    print(name)
    y += 1
print(f"Total number of employees in their 30's: {y}")

print()

z = 0
print("Employees in their 20's")
for name in age_twenty:
    print(name)
    z += 1
print(f"Total number of employees in their 30's: {z}")
