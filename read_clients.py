def main():
    infile = open('clients.txt', 'r')
    num = 1

    for line in infile:
        print(num, line)
        num += 1
        
        
main() 


