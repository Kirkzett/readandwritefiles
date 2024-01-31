import csv 

customers = open('customers.csv','r')
outfile = open('customer_country.csv','w')

csv_file = csv.reader(customers)

outfile.write("Full Name, Country" + "\n")
              
              

next(csv_file)
num = 0
#write new lines
for rec in csv_file:
    outfile.write(f"{rec[1]} {rec[2]}, {rec[4]} \n")
    num += 1

outfile.close()

print(f"Total Cusotmers: {num}")


    




